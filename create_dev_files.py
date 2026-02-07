"""
Test script to create the stratified samples as specified in Stage 1.1 of plan-1.md
"""
import sys
import json
import pandas as pd
import time
import torch
torch.set_default_device('cpu')

from transformers import AutoModelForCausalLM, AutoTokenizer
from utils.evaluate_results import NO_ANSWER_MARKER, evaluate_results

sys.path.append('.')


def create_dev_sample(number_of_answerable, num_of_unanswerable, output_filename=None, source_data='data/squad2.0-dev-1000.csv'):
    """
    Create a stratified sample of SQuAD 2.0 data with specified numbers of answerable and unanswerable questions.
    
    Args:
        number_of_answerable (int): Number of answerable questions (is_impossible=False) to sample
        num_of_unanswerable (int): Number of unanswerable questions (is_impossible=True) to sample
        output_filename (str, optional): Name of the output file. If None, auto-generates based on sample size
        source_data (str): Path to the source CSV file (default: 'data/squad2.0-dev-1000.csv')
    
    Returns:
        str: Path to the created sample file in dev-data directory
    """
    # Read the source data
    df = pd.read_csv(source_data)
    
    # Separate answerable and unanswerable questions
    answerable = df[df['is_impossible'] == False]
    unanswerable = df[df['is_impossible'] == True]
    
    # Sample the specified numbers
    answerable_sample = answerable.sample(n=number_of_answerable, random_state=42)
    unanswerable_sample = unanswerable.sample(n=num_of_unanswerable, random_state=42)
    
    # Combine and shuffle
    combined_sample = pd.concat([answerable_sample, unanswerable_sample])
    combined_sample = combined_sample.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Generate output filename if not provided
    if output_filename is None:
        total_samples = number_of_answerable + num_of_unanswerable
        output_filename = f'dev-data/stratified_sample_{total_samples}.csv'
    else:
        # Ensure it's in dev-data directory
        if not output_filename.startswith('dev-data/'):
            output_filename = f'dev-data/{output_filename}'
    
    # Save to dev-data directory
    combined_sample.to_csv(output_filename, index=False)
    
    print(f'Created stratified sample: {output_filename}')
    print(f'  - Answerable questions: {number_of_answerable}')
    print(f'  - Unanswerable questions: {num_of_unanswerable}')
    print(f'  - Total: {len(combined_sample)}')
    
    return output_filename

if __name__ == '__main__':
    print("Creating dev samples for Stage 1.1...\n")
    
    # Create tiny_dev_12.csv: 8 answerable + 4 unanswerable
    print("=" * 60)
    tiny_dev = create_dev_sample(
        number_of_answerable=8,
        num_of_unanswerable=4,
        output_filename='tiny_dev_12.csv'
    )
    
    print("\n" + "=" * 60)
    # Create qa_bench_50.csv: 30 answerable + 20 unanswerable
    qa_bench = create_dev_sample(
        number_of_answerable=30,
        num_of_unanswerable=20,
        output_filename='qa_bench_50.csv'
    )
    
    print("\n" + "=" * 60)
    print("\n✓ Stage 1.1 complete! Created:")
    print(f"  1. {tiny_dev} - for rapid code verification")
    print(f"  2. {qa_bench} - for runtime benchmarking and threshold tuning")
