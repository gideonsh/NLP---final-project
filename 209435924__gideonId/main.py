import os
import json
import time
import torch
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

torch.set_default_device('cpu')
device = "cuda" if torch.cuda.is_available() else "cpu"

from utils.evaluate_results import NO_ANSWER_MARKER, evaluate_results
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessor, LogitsProcessorList

model_name = 'meta-llama/Llama-3.2-3B-Instruct'
tokenizer = AutoTokenizer.from_pretrained(model_name, token=True)
model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16, token=True)
model.config.pad_token_id = tokenizer.eos_token_id
tokenizer.pad_token_id = tokenizer.eos_token_id

# Optimize thread usage for CPU
torch.set_num_threads(os.cpu_count()-2)
final_answer_column = "final_answer"


def analyze_performance(results_file, trial_name=None, log_file='dev-data/trials_log.md', probability_threshold=None, bias_value=None):
    """
    Analyzes performance metrics for SQuAD results.

    Input:
        results_file: Path to a CSV file or a pandas DataFrame.
        trial_name: String name for the current run.
        log_file: Path to the markdown log file.
        probability_threshold: Gating threshold value used.
        bias_value: Logit bias value used.

    Output:
        Dictionary containing overall and per-category metrics.

    Algorithm Flow:
        1. Parse input data and separate by answerability.
        2. Calculate accuracy for unanswerable questions.
        3. Use evaluate_results for F1 and EM metrics.
        4. Calculate binary classification performance.
        5. Write detailed results and metrics to a log file.
    """
    
    # Check if input is a path or dataframe
    if isinstance(results_file, str):
        dataframe = pd.read_csv(results_file)
    else:
        dataframe = results_file
    
    # Standardize boolean format
    dataframe['is_impossible'] = dataframe['is_impossible'].astype(str).str.upper() == 'TRUE'
    
    # Filter for unanswerable questions
    no_answer_dataframe = dataframe[dataframe['is_impossible'] == True]
    
    # Filter for answerable questions
    has_answer_dataframe = dataframe[dataframe['is_impossible'] == False]
    
    # Calculate correct no-answer predictions
    no_answer_correct = (no_answer_dataframe[final_answer_column] == NO_ANSWER_MARKER).sum()
    no_answer_total = len(no_answer_dataframe)
    
    # Compute no-answer percentage
    no_answer_accuracy = no_answer_correct / no_answer_total if no_answer_total > 0 else 0.0
    
    # Calculate overall metrics
    if isinstance(results_file, str):
        overall_metrics = evaluate_results(results_file)
    else:
        # Create temporary file for evaluation
        temporary_file = 'dev-data/temp_results_all.csv'
        dataframe.to_csv(temporary_file, index=False)
        overall_metrics = evaluate_results(temporary_file)
        # Remove temporary file
        if os.path.exists(temporary_file):
            os.remove(temporary_file)
    
    # Calculate metrics for answerable questions
    if len(has_answer_dataframe) > 0:
        # Create temporary file for answerable subset
        has_answer_temporary_file = 'dev-data/temp_hasans.csv'
        has_answer_dataframe.to_csv(has_answer_temporary_file, index=False)
        has_answer_metrics = evaluate_results(has_answer_temporary_file, final_answer_column=final_answer_column)
        has_answer_f1 = has_answer_metrics.get('f1', 0.0)
        has_answer_exact_match = has_answer_metrics.get('exact', 0.0)
        # Remove temporary file
        if os.path.exists(has_answer_temporary_file):
            os.remove(has_answer_temporary_file)
    else:
        has_answer_f1 = 0.0
        has_answer_exact_match = 0.0
    
    # Count correct binary classifications
    has_answer_correct_binary = (has_answer_dataframe[final_answer_column] != NO_ANSWER_MARKER).sum()
    binary_correct_total = no_answer_correct + has_answer_correct_binary

    # Compute binary classification accuracy
    binary_accuracy = (binary_correct_total / len(dataframe)) * 100 if len(dataframe) > 0 else 0.0

    metrics = {
        'overall_em': overall_metrics.get('exact', 0.0),
        'overall_f1': overall_metrics.get('f1', 0.0),
        'noans_accuracy': no_answer_accuracy * 100,
        'hasans_f1': has_answer_f1,
        'hasans_em': has_answer_exact_match,
        'binary_accuracy': binary_accuracy,
        'binary_correct': int(binary_correct_total),
        'noans_total': no_answer_total,
        'hasans_total': len(has_answer_dataframe),
        'total_questions': len(dataframe)
    }
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    trial_name = trial_name or f"Trial_{timestamp.replace(' ', '_').replace(':', '-')}"
    
    # Initialize log file if missing
    if not os.path.exists(log_file):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Create header for log file
        with open(log_file, 'w', encoding='utf-8') as file_handle:
            file_handle.write("# SQuAD 2.0 Trials Log\n\n")
            file_handle.write("Tracks all trial runs for monitoring.\n\n")
            file_handle.write("---\n\n")
    
    # Write trial data to log
    with open(log_file, 'a', encoding='utf-8') as file_handle:
        file_handle.write(f"## {trial_name}\n")
        file_handle.write(f"**Timestamp:** {timestamp}\n\n")
        
        # Log parameter settings
        if probability_threshold is not None and bias_value is not None:
            file_handle.write(f"**Parameters:** prob_threshold={probability_threshold}, bias_value={bias_value}\n\n")
        
        file_handle.write(f"**Dataset:** {results_file if isinstance(results_file, str) else 'DataFrame'}\n\n")
        file_handle.write("### Metrics\n\n")
        file_handle.write("| Metric | Value |\n")
        file_handle.write("|--------|-------|\n")
        file_handle.write(f"| **Overall EM** | {metrics['overall_em']:.2f} |\n")
        file_handle.write(f"| **Overall F1** | {metrics['overall_f1']:.2f} |\n")
        file_handle.write(f"| **NoAns Accuracy** | {metrics['noans_accuracy']:.2f}% ({no_answer_correct}/{no_answer_total}) |\n")
        file_handle.write(f"| **HasAns F1** | {metrics['hasans_f1']:.2f} |\n")
        file_handle.write(f"| **HasAns EM** | {metrics['hasans_em']:.2f} |\n")
        file_handle.write(f"| **Total Questions** | {metrics['total_questions']} |\n")
        file_handle.write(f"| **Binary Classification** | {metrics['binary_accuracy']:.2f}% |\n")
        file_handle.write("\n### Detailed Results\n\n")
        file_handle.write("| Index | Question | Actual | Model Prediction | Margin | Status |\n")
        file_handle.write("|-------|----------|--------|------------------|--------|--------|\n")
        
        # Iterate over results for detailed logging
        for index, row in dataframe.iterrows():
            is_impossible = row['is_impossible']
            
            # Determine ground truth text
            if is_impossible:
                ground_truth_text = NO_ANSWER_MARKER
            else:
                try:
                    answer_data = row['answers']

                    # Parse answer JSON strings
                    if isinstance(answer_data, str):
                        answer_list = json.loads(answer_data)
                        ground_truth_text = answer_list[0]['text'] if answer_list else "EMPTY"
                    else:
                        ground_truth_text = str(answer_data)
                except:
                    ground_truth_text = "ERROR_PARSING"
            
            model_prediction = str(row[final_answer_column])

            # Compare prediction with ground truth
            status = "✅" if (model_prediction.strip().upper() == ground_truth_text.strip().upper()) else "❌"
            
            safe_question = str(row['question']).replace('|', '\\|').replace('\n', ' ')
            safe_ground_truth = ground_truth_text.replace('|', '\\|').replace('\n', ' ')
            safe_prediction = model_prediction.replace('|', '\\|').replace('\n', ' ')
            
            margin_value = row.get('margin', 'N/A')

            # Format margin as string
            try:
                margin_string = f"{float(margin_value):.4f}"
            except (ValueError, TypeError):
                margin_string = str(margin_value)
            
            file_handle.write(f"| {index} | {safe_question[:50]} | {safe_ground_truth} | {safe_prediction} | {margin_string} | {status} |\n")
        
        file_handle.write(f"\n**correct binary classification:** {metrics['binary_accuracy']:.2f}%\n\n")
        
        # Add performance warning
        if metrics['noans_accuracy'] > 80 and metrics['hasans_f1'] < 50:
            file_handle.write("⚠️ **WARNING: Potential Over-correction Detected!**\n\n")
        
        file_handle.write("---\n\n")
    
    return metrics


def post_process_answer(answer):
    """
    Cleans generated answers by removing formatting artifacts.

    Input:
    answer: The raw string generated by the model.

    Output:
    A cleaned answer string.

    Algorithm Flow:
    1. Strip leading and trailing whitespace.
    2. Remove any trailing punctuation marks.
    3. Remove leading articles and single characters.
    """
    if not answer or answer == "NO ANSWER":
        return answer
    
    cleaned = answer.strip()
    
    # Remove final periods
    if cleaned.endswith("."):
        cleaned = cleaned[:-1].strip()

    tokens = cleaned.split()

    # Process tokens for leading character cleanup
    if len(tokens) > 1:
        first_token = tokens[0]

        # Remove single leading characters
        if len(first_token) == 1 and first_token.isalpha() and first_token.upper() != "I":
            tokens = tokens[1:]
            cleaned = " ".join(tokens)
    
    return cleaned.strip()


class SQuADScoreBiasProcessor(LogitsProcessor):
    """
    Applies unnormalized probability score bias to restrict generation to context tokens.

    Input:
    valid_ids: Collection of token IDs found in the context.
    bias_value: Float value added to valid token unnormalized scores.

    Algorithm Flow:
    Iterate over the batch and add bias to allowed IDs.
    """
    def __init__(self, valid_ids, bias_value=20.0):
        self.valid_ids = list(valid_ids)
        self.bias_value = bias_value

    def __call__(self, input_ids, scores):
        """Adds bias to specific token scores."""

        # Update unnormalized scores for valid context tokens
        scores[:, self.valid_ids] += self.bias_value
        return scores

def squad_qa(data_filename):
    """
    Main QA execution loop using gating and biased generation.

    Input:
    data_filename: Path to the input SQuAD CSV file.

    Output:
    Path to the generated results CSV file.

    Algorithm Flow:
    1. Construct prompts for each question.
    2. Run initial inference to get token probabilities.
    3. Use probability margin to decide if answerable.
    4. If answerable, generate restricted to context tokens.
    5. Save results and return new filename.
    """
    dataframe = pd.read_csv(data_filename)
    no_token_id = tokenizer.convert_tokens_to_ids("NO")
    probability_threshold = 0.01
    bias_value = 20.0
    final_answers = []
    margins = []

    # Process each row in the dataset
    for index, row in dataframe.iterrows():

        # Setup prompt messages
        messages = [
            {"role": "system", "content": "Extract the answer from text. Output ONLY the answer. If the answer is not there, say 'NO ANSWER'."},
            {"role": "user", "content": f"Context: {row['context']}\nQuestion: {row['question']}"},
        ]

        # Format messages into model-specific prompt
        prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)

        # Tokenize and prepare model inputs
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        # Run model execution for gating logic
        with torch.no_grad():
            gate_result = model.generate(
                **inputs,
                max_new_tokens=1,
                output_scores=True,
                return_dict_in_generate=True,
                temperature=1.5,
                use_cache=True, 
                pad_token_id=tokenizer.eos_token_id # Control marker
            )
            
            # Extract first token unnormalized scores
            unnormalized_scores = gate_result.scores[0][0]
            probabilities = torch.softmax(unnormalized_scores, dim=-1)

            # Get token IDs appearing in context
            context_ids = tokenizer.encode(row['context'], add_special_tokens=False)
            context_ids_with_space = tokenizer.encode(" " + row['context'], add_special_tokens=False)
            content_token_ids = list(set(context_ids + context_ids_with_space))

            no_probability = probabilities[no_token_id].item()
            
            # Compute margin between 'NO' and content signal.
            # Sum Top-5 content tokens to robustly detect answer intent and counter the model's 'NO' bias.
            if content_token_ids:
                phrase_probability = torch.topk(probabilities[content_token_ids], min(5, len(content_token_ids))).values.sum().item()
                margin = no_probability - phrase_probability
            else:
                margin = 1.0

        # Decision based on probability margin
        if margin > probability_threshold:
            final_answer = NO_ANSWER_MARKER
        
        else:
            # Prepare allowed IDs for extraction
            valid_ids = list(set(content_token_ids + [no_token_id, tokenizer.eos_token_id]))
            processors = LogitsProcessorList([SQuADScoreBiasProcessor(valid_ids, bias_value=bias_value)])

            # Create validity filter for combined sequence (input + first generated token)
            combined_validity_filter = torch.ones(gate_result.sequences.shape, device=model.device)

            # Generate restricted answer text using calculation memory buffer (KV cache)
            with torch.no_grad():
                outputs = model.generate(
                    gate_result.sequences,
                    attention_mask=combined_validity_filter,
                    max_new_tokens=12,
                    do_sample=False,
                    logits_processor=processors,
                    past_key_values=gate_result.past_key_values,
                    use_cache=True,
                    pad_token_id=tokenizer.eos_token_id # Control marker
                )
            
            # Decode generated answer
            generated_text = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True).strip()

            # Clean up output
            generated_text = post_process_answer(generated_text)
            final_answer = "NO ANSWER" if (not generated_text or "NO ANSWER" in generated_text.upper()) else generated_text

        final_answers.append(final_answer)
        margins.append(margin)

    # Store results in dataframe
    dataframe['final_answer'] = final_answers
    dataframe['margin'] = margins

    # Save output to disk
    dataframe.to_csv(data_filename.replace('.csv', '-results.csv'), index=False)

    return data_filename.replace('.csv', '-results.csv')


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

    elapsed_time = time.time() - start_time
    print(f"time: {elapsed_time: .2f} sec")
