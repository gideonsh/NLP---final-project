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

## Stage 2: Answerability Classification (Contrastive Gate)

**Goal:** Mathematically determine answerability using a distinct, unbiased forward pass to calculate a contrastive margin.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input_ids` | `torch.Tensor` | Tokenized context + question prompt |
| `logits` | `torch.Tensor` | Raw unbiased output scores for the first generated token |
| `no_ans_token_id` | `int` | The specific ID for the "NO" token in Llama-3.2's vocabulary |
| `contrastive_margin` | `float` | The difference between the logit of the "NO" token and the average of the Top-3 logits of all content tokens |
| `threshold` | `float` | The calibrated value used to decide if the model is confident enough to answer |

### Logic

1. Perform a distinct, **unbiased** forward pass with `max_new_tokens=1`.
2. Extract the logits for the "NO" token and determine the average of the Top-3 logits among all content-bearing tokens.
3. Calculate the **Contrastive Margin**: `Margin = Logit(NO) - avg(Top-3 Logit(Content))`.
4. If `Margin > threshold`, immediately terminate and return `NO_ANSWER_MARKER`.

---

## Stage 3: Grounded Extraction (Decoupled Logit-Bias)

**Goal:** Extract the answer span while forcing the model to remain strictly grounded, using a separate pass to prevent bias leakage into the classification stage.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `logit_bias` | `dict` | A mapping of token IDs to bias values to penalize non-contextual or hallucinatory tokens |
| `kv_cache` | `tuple/Cache` | The hijacked `past_key_values` from the Stage 2 gating pass |
| `temperature` | `float` | Set to 0.1 for near-deterministic, greedy decoding to ensure consistency |
| `max_new_tokens` | `int` | Capped to 20-30 tokens to minimize CPU runtime and prevent rambling |

### Logic (Decoupled Strategy)

- **Grounded Extraction (KV Reuse):** This stage is only executed if Stage 2 determines the question is answerable.
- **Logit-Bias & Cache Hijacking:** We apply the `LogitsProcessor` to the logits fetched in Stage 2, sample the first token manually, and then resume generation using the `past_key_values`.
- **Eliminating Redundancy:** By reusing the KV cache, we bypass the expensive prefill (prompt-processing) phase in `model.generate()`, effectively halving the latency of the extraction phase.
- **Prevention of Bleed:** By decoupling this pass from the classification pass in Stage 2, we prevent biased logits from sabotaging the model's natural classification signal.
- **Instruction Following:** The prompt will explicitly state: *"Extract the answer from the text. If it is not there, say 'NO ANSWER'."*

---

## Summary of the Engineering Rationale

| Stage | Decision | Why? |
|-------|----------|------|
| **Stage 1** | Balanced Sampling | To detect if our NoAns gains are hurting HasAns (Gideon's mistake) |
| **Stage 2** | Contrastive Gating | Uses a dedicated unbiased forward pass to calculate the margin between "NO" and content tokens. |
| **Stage 3** | KV Cache Hijack | Reuses the gating pass math to eliminate redundant prefill computation, making extraction 2x faster. |
| **Global** | Decoupled Architecture | Decouples classification from extraction to maximize binary accuracy and prevent infinite margins. |

---

# Change Log: Transformation to Decoupled Inference Architecture

## Overview
The implementation strategy has moved from a unified flow to a decoupled architecture to improve binary classification accuracy for unanswerable questions.

## Description (Before vs. After)

| Feature | Before (Unified / Biased) | After (Decoupled Architecture) |
| :--- | :--- | :--- |
| **Inference Flow** | Combined logprob extraction and generation in single pass. | Two-stage decoupled passes: one for classification, one for extraction. |
| **Stage 2 Signal** | Logprobs potentially influenced by subsequent generation biases. | Distinct, **unbiased** forward pass specifically for classification. |
| **Margin Calculation** | Simple probability check (`P(NO) > threshold`). | **Contrastive Margin**: Difference between "NO" token and the average of the Top-3 content tokens. |
| **Logic Isolation** | Biased logits from Stage 3 could "bleed" into Stage 2. | Total isolation; Logit-Bias Processor is restricted to Stage 3 only. |
| **Stability** | Numerical instability (infinite margins) and "Gideon Over-correction". | High numerical stability and preservation of the model's natural classification signal. |
| **Performance** | Redundant prefill in both gating and generation steps. | **KV Cache Hijacking**: Reuses prefill math from Stage 2 in Stage 3 to eliminate redundant compute. |

## Rationale
The "Gideon Over-correction" occurred because biased logits sabotaged the natural signal of the model. By decoupling the classification (Stage 2) from the extraction (Stage 3), we ensure that the grounded extraction constraints do not interfere with the model's ability to accurately identify unanswerable questions. Furthermore, by hijacking the KV cache from the gating pass, we ensure this decoupled architecture is as efficient as a unified pass.
