import os
import json
import time
import torch
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv('HF_TOKEN')

torch.set_default_device('cpu')
from utils.evaluate_results import NO_ANSWER_MARKER, evaluate_results
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessor, LogitsProcessorList

model_name = 'meta-llama/Llama-3.2-3B-Instruct'
tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)
model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16, token=hf_token)
model.config.pad_token_id = tokenizer.eos_token_id
tokenizer.pad_token_id = tokenizer.eos_token_id

final_answer_column = "final_answer"


def analyze_performance(results_file, trial_name=None, log_file='dev-data/trials_log.md'):
    """
    Analyze performance of a SQuAD 2.0 QA trial with detailed metrics breakdown.
    """
    
    # Load data if it's a file path
    if isinstance(results_file, str):
        df = pd.read_csv(results_file)
    else:
        df = results_file
    
    # Ensure is_impossible is boolean
    df['is_impossible'] = df['is_impossible'].astype(str).str.upper() == 'TRUE'
    
    # Separate answerable and unanswerable questions
    noans_df = df[df['is_impossible'] == True]
    hasans_df = df[df['is_impossible'] == False]
    
    # Compute NoAns Accuracy: percentage of unanswerable questions correctly identified
    noans_correct = (noans_df[final_answer_column] == NO_ANSWER_MARKER).sum()
    noans_total = len(noans_df)
    noans_accuracy = noans_correct / noans_total if noans_total > 0 else 0.0
    
    # Compute HasAns metrics using the evaluate library
    # First, get overall metrics
    if isinstance(results_file, str):
        overall_metrics = evaluate_results(results_file)
    else:
        temp_file = 'dev-data/temp_results_all.csv'
        df.to_csv(temp_file, index=False)
        overall_metrics = evaluate_results(temp_file)
        if os.path.exists(temp_file):
            os.remove(temp_file)
    
    # For HasAns F1, we need to compute it separately
    # Create a temporary file with only answerable questions
    if len(hasans_df) > 0:
        hasans_temp_file = 'dev-data/temp_hasans.csv'
        hasans_df.to_csv(hasans_temp_file, index=False)
        hasans_metrics = evaluate_results(hasans_temp_file, final_answer_column=final_answer_column)
        hasans_f1 = hasans_metrics.get('f1', 0.0)
        hasans_em = hasans_metrics.get('exact', 0.0)
        # Clean up temp file
        if os.path.exists(hasans_temp_file):
            os.remove(hasans_temp_file)
    else:
        hasans_f1 = 0.0
        hasans_em = 0.0
    
    # Binary Classification Accuracy (Answerable vs Unanswerable)
    # TP: is_impossible=True and pred='NO ANSWER'
    # TN: is_impossible=False and pred!='NO ANSWER'
    hasans_correct_binary = (hasans_df[final_answer_column] != NO_ANSWER_MARKER).sum()
    binary_correct = noans_correct + hasans_correct_binary
    binary_accuracy = (binary_correct / len(df)) * 100 if len(df) > 0 else 0.0

    # Compile results
    metrics = {
        'overall_em': overall_metrics.get('exact', 0.0),
        'overall_f1': overall_metrics.get('f1', 0.0),
        'noans_accuracy': noans_accuracy * 100,  # Convert to percentage
        'hasans_f1': hasans_f1,
        'hasans_em': hasans_em,
        'binary_accuracy': binary_accuracy,
        'binary_correct': int(binary_correct),
        'noans_total': noans_total,
        'hasans_total': len(hasans_df),
        'total_questions': len(df)
    }
    
    # Log to persistent file (append mode)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    trial_name = trial_name or f"Trial_{timestamp.replace(' ', '_').replace(':', '-')}"
    
    # Create log file with header if it doesn't exist
    if not os.path.exists(log_file):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write("# SQuAD 2.0 Trials Log\n\n")
            f.write("This file tracks all trial runs to monitor improvements and avoid over-correction.\n\n")
            f.write("---\n\n")
    
    # Append trial results
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"## {trial_name}\n")
        f.write(f"**Timestamp:** {timestamp}\n\n")
        f.write(f"**Dataset:** {results_file if isinstance(results_file, str) else 'DataFrame'}\n\n")
        f.write("### Metrics\n\n")
        f.write("| Metric | Value |\n")
        f.write("|--------|-------|\n")
        f.write(f"| **Overall EM** | {metrics['overall_em']:.2f} |\n")
        f.write(f"| **Overall F1** | {metrics['overall_f1']:.2f} |\n")
        f.write(f"| **NoAns Accuracy** | {metrics['noans_accuracy']:.2f}% ({noans_correct}/{noans_total}) |\n")
        f.write(f"| **HasAns F1** | {metrics['hasans_f1']:.2f} |\n")
        f.write(f"| **HasAns EM** | {metrics['hasans_em']:.2f} |\n")
        f.write(f"| **Total Questions** | {metrics['total_questions']} (HasAns: {metrics['hasans_total']}, NoAns: {metrics['noans_total']}) |\n")
        f.write(f"| **Binary Classification** | {metrics['binary_accuracy']:.2f}% ({metrics['binary_correct']}/{metrics['total_questions']}) |\n")
        f.write("\n")
        # Add detailed results table
        f.write("### Detailed Results\n\n")
        f.write("| Index | Question | Actual Answer | Model Prediction | Status |\n")
        f.write("|-------|----------|---------------|------------------|--------|\n")
        
        for idx, row in df.iterrows():
            # Get Ground Truth
            is_impossible = row['is_impossible']
            if is_impossible:
                gt_text = NO_ANSWER_MARKER
            else:
                try:
                    # Parse JSON answers if it's a string representation of a list
                    ans_data = row['answers']
                    if isinstance(ans_data, str):
                        ans_list = json.loads(ans_data)
                        gt_text = ans_list[0]['text'] if ans_list else "EMPTY"
                    else:
                        gt_text = str(ans_data)
                except:
                    gt_text = "ERROR_PARSING"
            
            model_pred = str(row[final_answer_column])
            
            # Simple status check (EM equivalent)
            status = "✅" if (model_pred.strip().upper() == gt_text.strip().upper()) else "❌"
            
            # Clean text for table (remove pipe characters and newlines)
            safe_q = str(row['question']).replace('|', '\\|').replace('\n', ' ')
            safe_gt = gt_text.replace('|', '\\|').replace('\n', ' ')
            safe_pred = model_pred.replace('|', '\\|').replace('\n', ' ')
            
            # Use idx to match logging (0-indexed)
            line_num = idx
            f.write(f"| {line_num} | {safe_q[:50]}{'...' if len(safe_q) > 50 else ''} | {safe_gt} | {safe_pred} | {status} |\n")
        
        f.write("\n")
        f.write(f"**correct binary classification:** {metrics['binary_accuracy']:.2f}% ({metrics['binary_correct']}/{metrics['total_questions']})\n\n")
        
        # Add warning if there's potential over-correction
        if metrics['noans_accuracy'] > 80 and metrics['hasans_f1'] < 50:
            f.write("⚠️ **WARNING: Potential Over-correction Detected!**\n")
            f.write("High NoAns accuracy but low HasAns F1 suggests the model is too conservative.\n\n")
        
        f.write("---\n\n")
    
    # Print summary to console
    print(f"\n{'='*60}")
    print(f"Trial: {trial_name}")
    print(f"{'='*60}")
    print(f"Overall EM:        {metrics['overall_em']:.2f}")
    print(f"Overall F1:        {metrics['overall_f1']:.2f}")
    print(f"NoAns Accuracy:    {metrics['noans_accuracy']:.2f}% ({noans_correct}/{noans_total})")
    print(f"HasAns F1:         {metrics['hasans_f1']:.2f}")
    print(f"HasAns EM:         {metrics['hasans_em']:.2f}")
    print(f"Total Questions:   {metrics['total_questions']} (HasAns: {metrics['hasans_total']}, NoAns: {metrics['noans_total']})")
    print(f"correct binary classification: {metrics['binary_accuracy']:.2f}% ({metrics['binary_correct']}/{metrics['total_questions']})")
    
    if metrics['noans_accuracy'] > 80 and metrics['hasans_f1'] < 50:
        print(f"\nWARNING: Potential Over-correction Detected!")
        print(f"   High NoAns accuracy but low HasAns F1 suggests the model is too conservative.")
    
    print(f"{'='*60}\n")
    print(f"Results appended to: {log_file}\n")
    
    return metrics


# Define the processor outside or inside the function - Stage 3
class SQuADLogitBiasProcessor(LogitsProcessor):
    """
    Implements Stage 3 Grounded Extraction by applying a probabilistic bias 
    to context-derived tokens, preventing hallucinations.
    """
    def __init__(self, valid_ids, bias_value=20.0):
        # Convert to a list to allow for efficient tensor indexing
        self.valid_ids = list(valid_ids)
        self.bias_value = bias_value

    def __call__(self, input_ids, scores):
        """
        Applies a high positive bias to valid tokens during the generation loop.
        """
        # Step 7 (Revised): Vectorized bias application
        # Instead of masking 'out' bad tokens, we boost 'in' the good ones.
        # This prevents Softmax collapse and potential NaN errors.
        scores[:, self.valid_ids] += self.bias_value
        
        return scores

def squad_qa(data_filename):
    df = pd.read_csv(data_filename)
    no_token_id = tokenizer.convert_tokens_to_ids("NO")
    
    # 1. TUNING FOR 10/12: Lower threshold = Less Conservative
    # Lowering this ensures we don't 'Over-correct' on answerable questions.
    prob_threshold = 0.05 
    final_answers = []

    for idx, row in df.iterrows():
        # --- STAGE 1: Prompt Construction ---
        messages = [
            {"role": "system", "content": "Extract the answer from text. If not there, say 'NO ANSWER'. Make sure to use the exact same answer as in the text."},
            {"role": "user", "content": f"Context: {row['context']}\nQuestion: {row['question']}"},
        ]
        prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        # --- STAGE 2: Cached Single-Pass Gating (Efficiency Fix) ---
        with torch.no_grad():
            gate_res = model.generate(
                **inputs,
                max_new_tokens=1,
                output_scores=True,
                return_dict_in_generate=True,
                use_cache=True, # Essential for < 20s runtime
                pad_token_id=tokenizer.eos_token_id
            )
            
            # Extract unbiased probabilities
            logits = gate_res.scores[0][0]
            probs = torch.softmax(logits, dim=-1)
            
            # Get valid IDs for the margin calculation
            ctx_ids = tokenizer.encode(row['context'], add_special_tokens=False)
            ctx_ids_sp = tokenizer.encode(" " + row['context'], add_special_tokens=False)
            content_ids = list(set(ctx_ids + ctx_ids_sp))
            
            no_prob = probs[no_token_id].item()
            
            # ELITE ACCURACY TWEAK: Sum Top-5 content tokens
            # This 'Phrase Signal' helps counter the model's 'NO' bias.
            if content_ids:
                phrase_prob = torch.topk(probs[content_ids], min(5, len(content_ids))).values.sum().item()
                prob_margin = no_prob - phrase_prob
            else:
                prob_margin = 1.0

        # --- THE GATE DECISION ---
        if prob_margin > prob_threshold:
            final_answer = "NO ANSWER"
            print(f"[{idx}] GATE: CLOSED (Margin: {prob_margin:.4f})")
        else:
            # --- STAGE 3: Resumed Grounded Generation ---
            valid_ids = list(set(content_ids + [no_token_id, tokenizer.eos_token_id]))
            processors = LogitsProcessorList([SQuADLogitBiasProcessor(valid_ids, bias_value=15.0)])

            # FIX: Create an attention mask for the combined sequence (input + first generated token)
            # gate_res.sequences contains the prompt + the 1 gate token
            combined_attention_mask = torch.ones(gate_res.sequences.shape, device=model.device)

            with torch.no_grad():
                outputs = model.generate(
                    gate_res.sequences,
                    attention_mask=combined_attention_mask, # Pass the mask here
                    max_new_tokens=24,
                    do_sample=True,
                    temperature=0.1,
                    logits_processor=processors,
                    past_key_values=gate_res.past_key_values,
                    use_cache=True,
                    pad_token_id=tokenizer.eos_token_id
                )
            
            gen_text = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True).strip()
            final_answer = "NO ANSWER" if (not gen_text or "NO ANSWER" in gen_text.upper()) else gen_text
            print(f"[{idx}] GATE: OPEN (Margin: {prob_margin:.4f}) -> {final_answer}")

        final_answers.append(final_answer)

    df['final_answer'] = final_answers
    df.to_csv(data_filename.replace('.csv', '-results.csv'), index=False)
    return df

# Dev Main
if __name__ == '__main__':
    # Start tracking time for the verification run
    start_time = time.time()
    
    # Path to your existing dev file
    dev_file_path = 'dev-data/tiny_dev_12.csv'
    
    print(f"[START] Starting Dev-Verification on: {dev_file_path}")
    print("=" * 60)

    # Step 1: Execute the Elite QA Pipeline (Gating + Grounded Extraction)
    # This will process the 12 samples (approx. 2.5 minutes on CPU)
    out_filename = squad_qa(dev_file_path)

    print("\n" + "=" * 60)
    print("Step 2: Running Deep-Dive Analysis...")
    
    # Step 2: Call the analysis function to verify NoAns vs HasAns performance
    # trial_name helps distinguish this 'tiny' run in your trials_log.md
    metrics = analyze_performance(
        results_file=out_filename,
        trial_name=f"dev_trial_tiny_{datetime.now().strftime('%Y%m%d%H%M')}",
        log_file='dev-data/trials_log.md',
    )

    # Step 3: Final runtime report
    elapsed_time = time.time() - start_time
    print(f"\n[DONE] Verification Complete.")
    print(f"Total time for 12 samples: {elapsed_time:.2f} seconds")
    print(f"Average time per sample: {elapsed_time/12:.2f} seconds")
    print(f"Results saved to: {out_filename}")
    print("=" * 60)
