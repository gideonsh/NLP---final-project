import os
import time
from datetime import datetime
from main import squad_qa, analyze_performance

def run_parameter_sweeps():
    """
    Executes multiple trials with varying gating parameters.

    Input: None (Uses internal lists for sweeps).

    Output: None (Logs results to external files).

    Algorithm Flow:
    1. Define search grid for probability thresholds and score bias.
    2. Iterate through all parameter combinations.
    3. Run QA pipeline and performance analysis for each set.
    4. Print summary metrics for each trial completion.
    """
    probability_thresholds = [0.01, 0.05, 0.1, 0.5]
    bias_values = [10, 15, 20, 25, 30]
    
    test_file_name = 'tiny_dev_12'
    dev_file_path = f'dev-data/{test_file_name}.csv'
    
    # Iterate over probability thresholds
    for probability_threshold in probability_thresholds:

        # Iterate over score bias values
        for bias_value in bias_values:
            trial_name = f"Exp_P{probability_threshold}_B{bias_value}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            start_time = time.time()

            # Execute the QA pipeline loop
            output_filename = squad_qa(
                dev_file_path, 
                probability_threshold=probability_threshold, 
                bias_value=float(bias_value)
            )
            
            # Perform granular metric analysis
            metrics = analyze_performance(
                results_file=output_filename,
                trial_name=trial_name,
                log_file='dev-data/experiments-params-trials_log.md',
                probability_threshold=probability_threshold,
                bias_value=float(bias_value)
            )
            
            elapsed_seconds = time.time() - start_time
            print(f"[{trial_name}] Done in {elapsed_seconds:.2f}s | Binary Acc: {metrics['binary_accuracy']:.2f}%")

if __name__ == "__main__":
    print("Starting parameter experiments...")
    run_parameter_sweeps()
    print("Experiments complete.")
