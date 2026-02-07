# Data Format Summary

## Overview
This directory contains data files for the SQuAD 2.0 (Stanford Question Answering Dataset) project focused on unanswerable question detection. The dataset includes both the original SQuAD 2.0 data and processed samples with model predictions.

## Files in the Data Directory

### 1. `dev-v2.0.json` (4.37 MB)
**Format:** JSON  
**Purpose:** Original SQuAD 2.0 development set

**Structure:**
```json
{
  "version": "v2.0",
  "data": [
    {
      "title": "Article Title",
      "paragraphs": [
        {
          "context": "The context paragraph text...",
          "qas": [
            {
              "question": "Question text?",
              "id": "unique_question_id",
              "answers": [
                {
                  "text": "Answer text",
                  "answer_start": 123
                }
              ],
              "is_impossible": false,
              "plausible_answers": [...]  // Only for impossible questions
            }
          ]
        }
      ]
    }
  ]
}
```

**Key Features:**
- Nested JSON structure with hierarchical organization
- Contains multiple articles, each with multiple paragraphs
- Each paragraph has multiple question-answer pairs (qas)
- **Answerable questions** have `"is_impossible": false` and contain `answers` array
- **Unanswerable questions** have `"is_impossible": true`, empty `answers` array, and `plausible_answers` field
- Answer positions are marked with character offsets (`answer_start`)
- Single-line JSON (not formatted for readability)

---

### 2. `squad2.0-dev-1000.csv` (751 KB, 1001 rows)
**Format:** CSV  
**Purpose:** Flattened sample of 1000 questions from the development set

**Structure:**
```csv
article,context,question,is_impossible,answers
0,"Context text...","Question?",FALSE,"[{""text"": ""Answer"", ""answer_start"": 123}]"
```

**Columns:**
1. **article** (integer): Article index/ID
2. **context** (string): The paragraph context containing the answer
3. **question** (string): The question text
4. **is_impossible** (boolean): TRUE/FALSE indicating if question is unanswerable
5. **answers** (JSON string): Stringified JSON array of answer objects

**Key Features:**
- Flattened representation of the nested JSON structure
- Each row represents a single question-answer pair
- Contains both answerable and unanswerable questions
- Answers field contains JSON-encoded array even in CSV format
- 1000 sample questions from the full development set
- Easier to process with pandas/data analysis tools

---

### 3. `squad2.0-dev-1000-sample-results.csv` (43 KB, 52 rows)
**Format:** CSV  
**Purpose:** Model predictions on a subset of the 1000-question sample

**Structure:**
```csv
article,context,question,is_impossible,answers,final answer
3,"Context...","Question?",True,[],NO ANSWER
```

**Columns:**
1. **article** (integer): Article index/ID (same as squad2.0-dev-1000.csv)
2. **context** (string): The paragraph context
3. **question** (string): The question text
4. **is_impossible** (boolean): Ground truth label
5. **answers** (JSON string): Ground truth answers
6. **final answer** (string): **NEW COLUMN** - Model's predicted answer

**Key Features:**
- Contains only 51 questions (subset of the 1000-question sample)
- Includes model predictions in the `final answer` column
- Model predictions are either:
  - `"NO ANSWER"` - Model predicts the question is unanswerable
  - Actual answer text - Model provides an answer
- Allows comparison between ground truth (`is_impossible`, `answers`) and predictions (`final answer`)
- Used for evaluating model performance on the unanswerable question detection task

---

## Key Differences Between Files

### Format Differences

| Aspect | dev-v2.0.json | squad2.0-dev-1000.csv | squad2.0-dev-1000-sample-results.csv |
|--------|---------------|----------------------|-------------------------------------|
| **Format** | JSON (nested) | CSV (flat) | CSV (flat) |
| **Size** | 4.37 MB | 751 KB | 43 KB |
| **Records** | Full dev set | 1000 questions | 51 questions |
| **Structure** | Hierarchical | Tabular | Tabular |
| **Predictions** | No | No | Yes (final answer column) |

### Content Differences

1. **dev-v2.0.json**
   - Complete, unprocessed SQuAD 2.0 development set
   - Preserves full hierarchical structure (articles → paragraphs → questions)
   - Contains all metadata and original formatting
   - Includes `plausible_answers` for impossible questions

2. **squad2.0-dev-1000.csv**
   - Sampled subset (1000 questions)
   - Flattened structure for easier processing
   - Loses article/paragraph hierarchy
   - Retains all question-answer information
   - No model predictions

3. **squad2.0-dev-1000-sample-results.csv**
   - Further subset (51 questions from the 1000)
   - Includes model predictions (`final answer` column)
   - Used for evaluation and analysis
   - Allows direct comparison of predictions vs. ground truth

### Question Types

All files contain two types of questions:

1. **Answerable Questions**
   - `is_impossible: false` (or `FALSE` in CSV)
   - Contains answer text and position
   - Example: "Who did Alexander I marry?" → "Sybilla of Normandy"

2. **Unanswerable Questions**
   - `is_impossible: true` (or `TRUE` in CSV)
   - Empty answers array: `[]`
   - Example: "Who did King David I of Scotland Marry?" → No answer in context

### Use Cases

- **dev-v2.0.json**: Original reference data, full evaluation, preserving document structure
- **squad2.0-dev-1000.csv**: Development/training sample, data exploration, baseline testing
- **squad2.0-dev-1000-sample-results.csv**: Model evaluation, performance analysis, error analysis

## Data Processing Pipeline

```
dev-v2.0.json (Original)
    ↓
    [Sampling & Flattening]
    ↓
squad2.0-dev-1000.csv (1000 samples)
    ↓
    [Model Inference on subset]
    ↓
squad2.0-dev-1000-sample-results.csv (51 samples with predictions)
```

## Notes

- The CSV files use escaped quotes for JSON-formatted fields (e.g., answers column)
- Article IDs are consistent across CSV files for tracking
- The results file shows model performance on both answerable and unanswerable questions
- "NO ANSWER" predictions should align with `is_impossible: TRUE` for correct predictions
