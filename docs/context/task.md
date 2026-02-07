# Project Overview: SQuAD 2.0 Unanswerability Detection

This project, assigned by **The Academic College of Tel Aviv-Yafo**, focuses on a critical challenge in Natural Language Processing (NLP): improving how Large Language Models (LLMs) handle questions that cannot be answered based on a given text.

---

## 🎯 Core Goal

The primary objective is to **improve the detection of unanswerable questions** in the SQuAD 2.0 dataset while performing content-grounded question answering. You must ensure the model accurately identifies when a context does not contain the answer, without significantly degrading its performance on answerable questions.

---

## 📋 Task Specifications

The task follows a standard content-grounded QA format:

- **Context**: A short passage provided to the model.
- **Question**: A query based on that specific passage.
- **Answer**: A response strictly grounded in the passage. If the passage does not contain the answer, the model must respond with **"NO ANSWER"**.

### Example Scenarios

| Question Type | Context Hint | Correct Behavior |
|--------------|--------------|------------------|
| **Answerable** | "...bounded resources (such as time or space)..." | Provide the specific fact: "time or space". |
| **Unanswerable** | Context mentions all machines are "equally powerful." | Identify the contradiction/absence: "NO ANSWER". |

---

## 🔧 Technical Requirements

### 1. The Model

- **Model**: `meta-llama/Llama-3.2-3B-Instruct`
- **Environment**: The model is optimized to run locally on a laptop.
- **Constraint**: You are **not allowed** to use a second LLM to verify or answer the questions.

### 2. Provided Files

#### Data:
- `dev-v2.0.json`: The full SQuAD 2.0 development set.
- `squad2.0-dev-1000.csv`: A 1000-sample subset for your primary development.

#### Code:
- `query_model.py`: Example code for model interaction.
- `evaluate_results.py`: Utility for calculating metrics.
- `main.py`: The entry point for the project (**do not modify the `main()` function**).

### 3. Success Metrics

Your work will be evaluated based on the following:

- **Exact Match (EM)**
- **F1 Score**
- **Improvement**: You must significantly increase accuracy on non-answerable questions while maintaining high accuracy for answerable ones.

---

## 📦 Submission Deliverables

**Due Date**: February 21, 2026

You must submit:

1. **`main.py`**: Containing your implementation of the `squad_qa()` function.
2. **`squad2.0-dev-1000-results.csv`**: Your best results on the 1000-sample set, including a "final answer" column.
3. **Project Report (3-4 pages PDF)**:
   - Detailed explanation of your solution and experiments (what worked and what didn't).
   - Final accuracy report and error analysis.
   - Insights into "easy" vs. "difficult" cases.
   - Expected runtime for a 50-sample batch.

---

## ⚠️ Important Notes

- **Efficiency**: While there are no strict runtime limits, faster solutions will receive higher scores.
- **Creativity**: Out-of-the-box solutions and the use of external libraries (not mentioned in class) are encouraged.
- **Testing**: The project will be tested on multiple smaller, unseen samples (approx. 50 examples each).