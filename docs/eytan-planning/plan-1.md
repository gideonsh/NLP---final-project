# SQuAD 2.0 Unanswerability Detection - Implementation Plan

## Stage 1: Infrastructure & Benchmarking

**Goal:** Create a reproducible testing environment to quantify improvements.

### 1.1 Data Sampling

- **`tiny_dev_12.csv`**: Stratified sample of 8 answerable and 4 unanswerable questions
  - Use this for rapid code verification
  
- **`qa_bench_50.csv`**: Stratified sample of 30 answerable and 20 unanswerable questions
  - Use this for runtime benchmarking and logprob threshold tuning

### 1.2 The Trial Summarizer

Develop `analyze_performance(results_df)` to compute metrics beyond the global F1/EM.

**Metrics:**
- Overall EM/F1
- NoAns Accuracy (Success on `is_impossible: True`)
- HasAns F1 (Success on `is_impossible: False`)

**Goal:** Ensure we don't repeat the "Gideon Over-correction" (where high NoAns accuracy killed HasAns performance).

---

## Stage 2: Answerability Classification (Logprob Gate)

**Goal:** Mathematically determine answerability using the model's internal probability distribution (Softmax).

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input_ids` | `torch.Tensor` | Tokenized context + question prompt |
| `logits` | `torch.Tensor` | Raw output scores for the first generated token |
| `no_ans_token_id` | `int` | The specific ID for the "NO" token in Llama-3.2's vocabulary |
| `threshold` | `float` | The calibrated value (tuned via sklearn) used to decide if the model is confident enough to answer |

### Logic

1. Perform a single forward pass with `max_new_tokens=1`
2. Extract the log-probability of the token "NO" (representing "NO ANSWER") versus the highest-scoring content token
3. If `P(NO) > threshold`, immediately terminate and return `NO_ANSWER_MARKER`

---

## Stage 3: Grounded Extraction (Strategy 1: Logit-Bias Gate)

**Goal:** Extract the answer span while forcing the model to remain strictly grounded, using Strategy 1 to prevent hallucinations.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `logit_bias` | `dict` | A mapping of token IDs to bias values to penalize non-contextual or hallucinatory tokens |
| `temperature` | `float` | Set to 0.1 for near-deterministic, greedy decoding to ensure consistency |
| `max_new_tokens` | `int` | Capped to 20-30 tokens to minimize CPU runtime and prevent rambling |

### Logic (Elite Strategy 1)

- **Contextual Constraint:** We will use Strategy 1 to bias the model's logits toward tokens actually present in the provided context
- **Instruction Following:** The prompt will explicitly state: *"Extract the answer from the text. If it is not there, say 'NO ANSWER'."*
- **Single-Pass Efficiency:** By using the logprobs from Stage 2 and the generation from Stage 3 in a unified flow, we stay within the 10–15 minute limit for 50 samples on the CPU

---

## Summary of the Engineering Rationale

| Stage | Decision | Why? |
|-------|----------|------|
| **Stage 1** | Balanced Sampling | To detect if our NoAns gains are hurting HasAns (Gideon's mistake) |
| **Stage 2** | Logprob Gating | Uses the Softmax theory from lectures to catch unanswerability before the model "guesses" |
| **Stage 3** | Logit-Bias Extraction | Replaces "Strict Grounding" (which failed due to casing/formatting) with a probabilistic bias toward context words |
| **Global** | sklearn/torch | Leveraging required libraries for mathematical threshold calibration rather than "guessing" a cutoff |