import json
import pandas as pd
import time
import torch
torch.set_default_device('cpu')
import os
from datetime import datetime

device = "cuda" if torch.cuda.is_available() else "cpu"
hf_token = os.getenv("HF_TOKEN")  # optional if you already did huggingface-cli login

from transformers import AutoModelForCausalLM, AutoTokenizer
from utils.evaluate_results import NO_ANSWER_MARKER, evaluate_results


model_name = 'meta-llama/Llama-3.2-3B-Instruct'
# tokenizer = AutoTokenizer.from_pretrained(model_name, token=True)
# model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16, token=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)
model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16, token=hf_token).to(device)
model.config.pad_token_id = tokenizer.eos_token_id
tokenizer.pad_token_id = tokenizer.eos_token_id

final_answer_column = "final answer"


# def squad_qa(data_filename):

#     # todo: implement this function, design your solution and document properly

#     # todo: you will need to sign up for huggingface and visit https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct to get access
#     # todo: squad2.0 dataset - https://huggingface.co/datasets/rajpurkar/squad_v2


#     out_filename = data_filename.replace('.csv', '-results.csv')
#     print(f'final answers recorded into {out_filename}')
#     return out_filename

def squad_qa(data_filename):
    df = pd.read_csv(data_filename)

    final_answers = []
    for index, row in df.iterrows():
        messages = [
            {
                "role": "system",
                "content": "answer the question according to the context. If you don't know, return 'NO ANSWER'"
            },
            {
                "role": "user",
                "content": f"Context:\n{row['context']}\n\nQuestion:\n{row['question']}\n",
            },
        ]

        prompt = tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=False
        )
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        with torch.no_grad():
            out = model.generate(
                **inputs,
                max_new_tokens=24,
                do_sample=False,  # deterministic baseline
                pad_token_id=tokenizer.eos_token_id,
            )

        gen = tokenizer.decode(
            out[0][inputs["input_ids"].shape[-1]:],
            skip_special_tokens=True
        ).strip()

        # tiny cleanup to keep “raw baseline” usable
        gen = gen.splitlines()[0].strip()
        if gen.lower().startswith("answer:"):
            gen = gen[len("answer:"):].strip()

        if (not gen) or ("no answer" in gen.lower()):
            gen = NO_ANSWER_MARKER

        print(f"[{index}] {row['question']} -----> {gen}")
        final_answers.append(gen)

    # IMPORTANT: match your current evaluate call: final_answer_column='final answer'
    df["final answer"] = final_answers

    out_filename = data_filename.replace(".csv", "-results.csv")
    df.to_csv(out_filename, index=False)

    print(f"final answers recorded into {out_filename}")
    return out_filename


def analyze_performance(results_file, trial_name=None, log_file='dev-data/trials_log.md', prob_threshold=None, bias_value=None):
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
        overall_metrics = evaluate_results(results_file, final_answer_column=final_answer_column)
    else:
        temp_file = 'dev-data/temp_results_all.csv'
        df.to_csv(temp_file, index=False)
        overall_metrics = evaluate_results(temp_file, final_answer_column=final_answer_column)
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
        if prob_threshold is not None and bias_value is not None:
            f.write(f"**Parameters:** prob_threshold={prob_threshold}, bias_value={bias_value}\n\n")
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
        f.write("| Index | Question | Actual Answer | Model Prediction | Margin | Status |\n")
        f.write("|-------|----------|---------------|------------------|--------|--------|\n")
        
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
            
            # Get margin if it exists
            margin_val = row.get('margin', 'N/A')
            try:
                margin_str = f"{float(margin_val):.4f}"
            except (ValueError, TypeError):
                margin_str = str(margin_val)
            
            # Use idx to match logging (0-indexed)
            line_num = idx
            f.write(f"| {line_num} | {safe_q[:50]}{'...' if len(safe_q) > 50 else ''} | {safe_gt} | {safe_pred} | {margin_str} | {status} |\n")
        
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
    
    # Print detailed evaluate_results metrics
    if isinstance(results_file, str):
        eval_out = evaluate_results(results_file, final_answer_column=final_answer_column)
        eval_out_list = [str((k, round(v, 3))) for (k, v) in eval_out.items()]
        print("Detailed Metrics:")
        print('\n'.join(eval_out_list))
        print(f"{'='*60}\n")

    print(f"Results appended to: {log_file}\n")
    
    return metrics



if __name__ == '__main__':
    start_time = time.time()

    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

    data = pd.read_csv(config['data'])
    sample = data.sample(n=config['sample_for_solution'])  # for grading will be replaced with 'sample_for_grading'
    sample_filename = config['data'].replace('.csv', '-sample.csv')
    sample.to_csv(sample_filename, index=False)

    out_filename = squad_qa(sample_filename)  # todo: the function you implement

    eval_out = evaluate_results(out_filename, final_answer_column='final answer')
    eval_out_list = [str((k, round(v, 3))) for (k, v) in eval_out.items()]
    print('\n'.join(eval_out_list))
    # Deep-dive Analysis
    metrics = analyze_performance(
        results_file=out_filename,
        trial_name=f"new_main_trial_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        log_file='dev-data/trials_log.md'
    )

    elapsed_time = time.time() - start_time
    print(f"time: {elapsed_time: .2f} sec")