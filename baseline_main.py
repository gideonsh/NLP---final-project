import json
import pandas as pd
import time
import torch
import os
from datetime import datetime

torch.set_default_device('cpu')
device = "cuda" if torch.cuda.is_available() else "cpu"
huggingface_token = os.getenv("HF_TOKEN")

from transformers import AutoModelForCausalLM, AutoTokenizer
from utils.evaluate_results import NO_ANSWER_MARKER, evaluate_results

model_name = 'meta-llama/Llama-3.2-3B-Instruct'
tokenizer = AutoTokenizer.from_pretrained(model_name, token=huggingface_token)
model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16, token=huggingface_token).to(device)
model.config.pad_token_id = tokenizer.eos_token_id
tokenizer.pad_token_id = tokenizer.eos_token_id

final_answer_column = "final answer"


def squad_qa(data_filename):
    """
    Baseline QA execution using simple prompt formatting.

    Input:
    data_filename: Path to the input SQuAD CSV file.

    Output:
    Path to the generated results CSV file.

    Algorithm Flow:
    1. Load dataset.
    2. Format prompt for each question.
    3. Run model execution to generate answer.
    4. Apply simple cleanup and save results.
    """
    dataframe = pd.read_csv(data_filename)
    final_answers = []

    # Process each row in the dataset
    for index, row in dataframe.iterrows():

        # Setup prompt messages
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

        # Format messages into model-specific prompt
        prompt = tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=False
        )

        # Tokenize and prepare model inputs
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        # Run model execution
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=24,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id, # Control marker
            )

        # Decode generated text
        generated_text = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[-1]:],
            skip_special_tokens=True
        ).strip()

        # Split and take first line
        generated_text = generated_text.splitlines()[0].strip()

        # Remove answer prefix if present
        if generated_text.lower().startswith("answer:"):
            generated_text = generated_text[len("answer:"):].strip()

        # Handle no-answer case
        if (not generated_text) or ("no answer" in generated_text.lower()):
            generated_text = NO_ANSWER_MARKER

        final_answers.append(generated_text)

    dataframe["final answer"] = final_answers
    output_filename = data_filename.replace(".csv", "-results.csv")

    # Save output to disk
    dataframe.to_csv(output_filename, index=False)

    return output_filename


def analyze_performance(results_file, trial_name=None, log_file='dev-data/trials_log.md', probability_threshold=None, bias_value=None):
    """
    Analyzes performance metrics for SQuAD results.

    Input:
    results_file: Path to a CSV file or a pandas DataFrame.
    trial_name: String name for the current run.
    log_file: Path to the markdown log file.
    probability_threshold: Threshold value used for decisions.
    bias_value: Score bias value used.

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
        overall_metrics = evaluate_results(results_file, final_answer_column=final_answer_column)
    else:

        # Create temporary file for evaluation
        temporary_file = 'dev-data/temp_results_all.csv'
        dataframe.to_csv(temporary_file, index=False)
        overall_metrics = evaluate_results(temporary_file, final_answer_column=final_answer_column)

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
        file_handle.write("| Index | Question | Actual | Model Prediction | Status |\n")
        file_handle.write("|-------|----------|--------|------------------|--------|\n")
        
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
            
            file_handle.write(f"| {index} | {safe_question[:50]} | {safe_ground_truth} | {safe_prediction} | {status} |\n")
        
        file_handle.write(f"\n**correct binary classification:** {metrics['binary_accuracy']:.2f}%\n\n")
        
        # Add performance warning
        if metrics['noans_accuracy'] > 80 and metrics['hasans_f1'] < 50:
            file_handle.write("⚠️ **WARNING: Potential Over-correction Detected!**\n\n")
        
        file_handle.write("---\n\n")
    
    return metrics


if __name__ == '__main__':
    start_time = time.time()

    # Load configuration
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

    dataframe_source = pd.read_csv(config['data'])

    # Prepare random sample
    sample_dataframe = dataframe_source.sample(n=config['sample_for_solution'])
    sample_filename = config['data'].replace('.csv', '-sample.csv')

    # Guard sample to disk
    sample_dataframe.to_csv(sample_filename, index=False)

    # Process sample
    output_filename = squad_qa(sample_filename)

    # Evaluate results
    eval_output = evaluate_results(output_filename, final_answer_column='final answer')
    eval_output_list = [str((k, round(v, 3))) for (k, v) in eval_output.items()]
    print('\n'.join(eval_output_list))

    # Run analysis
    metrics = analyze_performance(
        results_file=output_filename,
        trial_name=f"baseline_trial_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        log_file='dev-data/trials_log.md'
    )

    elapsed_time = time.time() - start_time
    print(f"time: {elapsed_time: .2f} sec")