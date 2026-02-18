"""
Script to create stratified samples for development and evaluation.
"""
import sys
import pandas as pd

def create_dev_sample(number_of_answerable, number_of_unanswerable, output_filename=None, source_data='data/squad2.0-dev-1000.csv'):
    """
    Creates a stratified sample of SQuAD 2.0 data.

    Input:
    number_of_answerable: Integer count of answerable questions to include.
    number_of_unanswerable: Integer count of unanswerable questions to include.
    output_filename: Optional string for the output path.
    source_data: Path to the source CSV file.

    Output:
    Path to the created sample file.

    Algorithm Flow:
    1. Filter source data by is_impossible flag.
    2. Randomly sample specified counts from each group.
    3. Combine subsets and shuffle the sequence.
    4. Save result to the dev-data directory.
    """
    # Read the source data
    dataframe = pd.read_csv(source_data)
    
    # Separate answerable and unanswerable questions
    answerable = dataframe[dataframe['is_impossible'] == False]
    unanswerable = dataframe[dataframe['is_impossible'] == True]
    
    # Sample the specified numbers
    answerable_sample = answerable.sample(n=number_of_answerable, random_state=42)
    unanswerable_sample = unanswerable.sample(n=number_of_unanswerable, random_state=42)
    
    # Combine and shuffle
    combined_sample = pd.concat([answerable_sample, unanswerable_sample])

    # Shuffle the dataset rows
    combined_sample = combined_sample.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Generate output filename if not provided
    if output_filename is None:
        total_samples = number_of_answerable + number_of_unanswerable
        output_filename = f'dev-data/stratified_sample_{total_samples}.csv'
    else:

        # Ensure it's in dev-data directory
        if not output_filename.startswith('dev-data/'):
            output_filename = f'dev-data/{output_filename}'
    
    # Save to dev-data directory
    combined_sample.to_csv(output_filename, index=False)
    
    return output_filename

if __name__ == '__main__':
    print("Creating dev samples...\n")
    
    # Create tiny_dev_12.csv
    print("=" * 60)
    tiny_dev = create_dev_sample(
        number_of_answerable=8,
        number_of_unanswerable=4,
        output_filename='tiny_dev_12.csv'
    )
    
    print(f'Created sample: {tiny_dev}')
    
    print("\n" + "=" * 60)

    # Create qa_bench_50.csv
    qa_bench = create_dev_sample(
        number_of_answerable=30,
        number_of_unanswerable=20,
        output_filename='qa_bench_50.csv'
    )

    print(f'Created sample: {qa_bench}')
    print("\n✓ Verification samples created.")
