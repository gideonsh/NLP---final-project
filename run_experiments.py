import os
import time
from datetime import datetime
from main import squad_qa, analyze_performance

def run_experiments():
    prob_thresholds = [0.01, 0.05, 0.1, 0.5]
    bias_values = [10, 15, 20, 25, 30]
    
    test_file_name = 'tiny_dev_12'
    dev_file_path = f'dev-data/{test_file_name}.csv'
    
    print(f"Starting experiments on {dev_file_path}")
    print(f"Total combinations: {len(prob_thresholds) * len(bias_values)}")
    
    for prob_t in prob_thresholds:
        for bias_v in bias_values:
            trial_name = f"Exp_P{prob_t}_B{bias_v}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            print(f"\n--- Running: {trial_name} ---")
            
            start_t = time.time()
            # Run the QA pipeline
            out_filename = squad_qa(dev_file_path, prob_threshold=prob_t, bias_value=float(bias_v))
            
            # Run analysis and log results
            metrics = analyze_performance(
                results_file=out_filename,
                trial_name=trial_name,
                log_file='dev-data/experiments-params-trials_log.md',
                prob_threshold=prob_t,
                bias_value=float(bias_v)
            )
            
            elapsed = time.time() - start_t
            print(f"Completed in {elapsed:.2f}s. Binary Acc: {metrics['binary_accuracy']:.2f}%")

if __name__ == "__main__":
    run_experiments()
