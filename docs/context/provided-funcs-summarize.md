# Provided Functions Summary

This document summarizes all the provided functions in the NLP final project codebase, organized by location.

---

## Main Module (`main.py`)

### `squad_qa(data_filename)`
**Location:** `main.py` (lines 18-28)

**Purpose:** Main function to implement the SQuAD 2.0 question-answering solution.

**Parameters:**
- `data_filename` (str): Path to the input CSV file containing SQuAD data

**Returns:**
- `out_filename` (str): Path to the output CSV file with results (input filename with '-results.csv' suffix)

**Current Status:** 
- Placeholder implementation (marked with TODO comments)
- Currently only generates the output filename and prints it
- Needs to be implemented with the actual QA solution

**Notes:**
- Requires HuggingFace account access to `meta-llama/Llama-3.2-3B-Instruct`
- Uses SQuAD 2.0 dataset from HuggingFace
- The function is called from the main execution block with a sampled dataset

---

## Utilities Module (`utils/`)

### `evaluate_results(datafile, final_answer_column='final_answer')`
**Location:** `utils/evaluate_results.py` (lines 9-57)

**Purpose:** Evaluate model predictions using the SQuAD v2.0 metric from HuggingFace's `evaluate` library.

**Parameters:**
- `datafile` (str): Path to CSV file containing ground-truth answers and model predictions
- `final_answer_column` (str, optional): Name of the column containing model's final answers (default: `'final_answer'`)

**Returns:**
- `results` (dict): Evaluation metrics including:
  - Exact Match (EM)
  - Token-level F1 score
  - Breakdowns for answerable vs. unanswerable examples

**Functionality:**
1. Loads the SQuAD v2.0 metric from HuggingFace
2. Reads CSV file with predictions and ground truth
3. Converts each row to the format expected by the metric:
   - **Predictions:** Contains `id`, `prediction_text`, and `no_answer_probability`
   - **References:** Contains `id` and `answers` with `text` and `answer_start` fields
4. Handles unanswerable questions using the `NO_ANSWER_MARKER` constant
5. Computes and returns evaluation results

**CSV Format Expected:**
- Must contain columns: `answers`, `is_impossible`, and the specified `final_answer_column`
- `answers` column should contain JSON-formatted answer data
- `is_impossible` column indicates if the question is unanswerable

**Special Handling:**
- Model answers matching `NO_ANSWER_MARKER` are treated as unanswerable (empty prediction with probability 1.0)
- Other answers are treated as answerable (with probability 0.0)

---

### Constants

#### `NO_ANSWER_MARKER`
**Location:** `utils/evaluate_results.py` (line 6)

**Value:** `'NO ANSWER'`

**Purpose:** Standard marker string to indicate when a question is unanswerable. Used by both the model output and the evaluation function to identify unanswerable questions.

---

## Example Scripts

### `utils/query_model.py`
**Location:** `utils/query_model.py` (lines 1-30)

**Purpose:** Example/template script demonstrating how to query the Llama 3.2 3B Instruct model.

**Functionality:**
1. Initializes the model and tokenizer for `meta-llama/Llama-3.2-3B-Instruct`
2. Sets up a chat template with system and user messages
3. Demonstrates the complete pipeline:
   - Applying chat template
   - Tokenizing input
   - Generating model response
   - Decoding output

**Configuration:**
- Uses CPU device (`torch.set_default_device('cpu')`)
- Model loaded with `float16` precision
- Generation parameters:
  - `max_new_tokens=50`
  - `do_sample=False` (deterministic generation)
- Padding token set to EOS token

**Example Usage:**
```python
messages = [
    {"role": "system", "content": "You are an QA assistant for the SQuAD2.0 dataset."},
    {"role": "user", "content": "Who are you?"},
]
```

**Note:** This is a demonstration script, not a function to be imported. It shows the pattern for interacting with the model that should be adapted in the main implementation.

---

## Main Execution Flow (`main.py` - `if __name__ == '__main__'`)

**Location:** `main.py` (lines 29-50)

**Purpose:** Entry point for the application that orchestrates the complete pipeline.

**Steps:**
1. **Load Configuration:** Reads `config.json` to get data path and sample size
2. **Sample Data:** Creates a random sample from the full dataset based on `sample_for_solution` parameter
3. **Save Sample:** Writes sampled data to a new CSV file
4. **Run QA:** Calls `squad_qa()` with the sample file
5. **Evaluate:** Calls `evaluate_results()` with the output file
6. **Display Results:** Prints evaluation metrics (rounded to 3 decimal places)
7. **Report Timing:** Displays total execution time

**Configuration Parameters (from `config.json`):**
- `data`: Path to the input CSV dataset
- `sample_for_solution`: Number of samples to use for development/testing
- Note: For grading, `sample_for_solution` will be replaced with `sample_for_grading`

---

## Global Model Setup (`main.py`)

**Location:** `main.py` (lines 11-16)

**Purpose:** Initialize the Llama model and tokenizer as global objects for reuse.

**Configuration:**
- Model: `meta-llama/Llama-3.2-3B-Instruct`
- Precision: `float16`
- Device: CPU (set via `torch.set_default_device('cpu')`)
- Padding: EOS token used as padding token

**Objects Created:**
- `tokenizer`: AutoTokenizer instance
- `model`: AutoModelForCausalLM instance

---

## Summary of Key Design Patterns

1. **Separation of Concerns:** 
   - Main logic in `main.py`
   - Evaluation utilities in separate module
   - Example code isolated in `query_model.py`

2. **Standardization:**
   - `NO_ANSWER_MARKER` constant ensures consistency
   - Standard CSV format for data exchange
   - HuggingFace evaluate library for metrics

3. **Flexibility:**
   - Configurable via `config.json`
   - Customizable final answer column name
   - Sample size control for testing vs. grading

4. **Model Efficiency:**
   - Global model initialization (load once, use many times)
   - CPU-based execution
   - Float16 precision for memory efficiency
