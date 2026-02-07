# Status Report: SQuAD 2.0 Unanswerable Detection Project
**Date:** February 5, 2026  
**Teammate:** Gideon  
**Project:** NLP Final Project - SQuAD 2.0 + Llama-3.2-3B-Instruct

---

## 📋 Task Overview

**Objective:** Improve detection of unanswerable questions in SQuAD 2.0 while maintaining strong performance on answerable questions.

**Model:** `meta-llama/Llama-3.2-3B-Instruct`  
**Primary Goal:** High NoAns (unanswerable) accuracy without hallucinations  
**Secondary Goal:** Maintain strong HasAns (answerable) performance  
**Constraint:** No second LLM allowed; extractive answers only

**Key Metrics:**
- Exact Match (EM)
- F1 Score
- HasAns_exact / HasAns_f1
- NoAns_exact / NoAns_f1

---

## 🗂️ Planning Versions Summary

### Version 1: Original Baseline Plan (`planning.MD` / `planningOld.MD`)
**Core Strategy:**
- Single-stage pipeline with strict post-processing
- Grounding gate: exact/fuzzy/regex matching to context
- Focus on extractive answers only
- Return `NO ANSWER` if output cannot be grounded

**Key Principles:**
1. Never hallucinate - strict grounding required
2. Keep answers extractive (shortest span from context)
3. Optimize runtime: GPU, batching, low `max_new_tokens`

### Version 2: Two-Stage Pipeline (`planningNew.MD`)
**Major Architecture Change:**
- **Stage A:** Answerability gating (YES/NO classification)
- **Stage B:** Answer generation (only for YES predictions)
- **Stage C:** Optional verifier (validate proposed answers)

**Context Handling:**
- Windowing with keyword-based scoring
- Top-k window selection for relevance

---

## 🧪 Experimental Trials

### **TRIAL 1: Single-Token Next-Logprob Gate** ❌ **FAILED**

**Implementation Details:**
```python
# Token resolution
_YES_TOKEN_ID = single token for "YES"
_NO_TOKEN_ID = single token for "NO"

# Gate logic: next-token logprob from last position
yes_lp - no_lp > ANSWERABLE_LOGIT_MARGIN
```

**Configuration:**
- `ANSWERABLE_LOGIT_MARGIN = 0.0`
- `BATCH_SIZE_CLASSIFY = 24`
- `BATCH_SIZE_ANSWER = 4`
- `MAX_NEW_TOKENS_ANSWER = 24`

**Results (n=50):**
```
Gate: YES=50/50 (100.0%)
exact: 36.0
f1: 39.667
HasAns_exact: 55.556
NoAns_exact: 13.043  ← CATASTROPHIC
Runtime: 618.79 sec
```

**Why It Failed:**
1. **Tokenization mismatch:** Llama tokenizers encode `"YES"` vs `" YES"` (with leading space) differently
2. **Prompt bias:** Model defaulted to "YES" without proper calibration
3. **Gate became useless:** Predicted answerable for ALL questions
4. **NoAns collapsed:** Only 13% accuracy on unanswerable questions

**Key Code Issue:**
```python
# Incorrect: single token may not match model's actual tokenization
yes_lp = logits[:, _YES_TOKEN_ID]
no_lp = logits[:, _NO_TOKEN_ID]
```

---

### **TRIAL 2: Multi-Token Completion Logprob Gate** ⚠️ **PARTIAL SUCCESS**

**Implementation Details:**
```python
# Token resolution (multi-token support)
_YES_TOKEN_IDS = tokenizer.encode("YES")  # May be multiple tokens
_NO_TOKEN_IDS = tokenizer.encode("NO")

# Completion logprob sum
def _completion_logprob_sum(model, input_ids, attn, completion_ids, pad_token_id):
    # Appends completion tokens and sums their log probabilities
    # Returns: tensor of shape [B] with total logprob for completion
```

**Configuration:**
- `ANSWERABLE_LOGIT_MARGIN = -0.5` (more permissive)
- `VERIFY_MARGIN = 0.3`
- `MAX_CTX_TOKENS_CLASSIFY = 256`
- `MAX_CTX_TOKENS_ANSWER = 900`
- `MAX_PROMPT_TOKENS_CAP = 1024`
- `WINDOW_STRIDE = 128`
- `TOPK_CLASSIFY_WINDOWS = 1`
- `TOPK_ANSWER_WINDOWS = 2`
- `BATCH_SIZE_CLASSIFY = 24`
- `BATCH_SIZE_ANSWER = 4`
- `MAX_NEW_TOKENS_ANSWER = 24`

**Pipeline:**
1. **Classify stage:** Build top-1 window → prompt → compute YES/NO logprob sums → gate decision
2. **Answer stage (for YES only):**
   - Try window #1 → generate → ground/shrink → verify
   - Retry failures with window #2
3. **Verification:** For each candidate answer, ask "Is it fully supported?" (YES/NO via logprob)

**Results (n=50):**
```
Gate: YES=31/50 (62.0%)
exact: 50.0
f1: 51.0
HasAns_exact: 25.926  ← TOO LOW
NoAns_exact: 78.261   ← STRONG IMPROVEMENT
Runtime: 600.94 sec
```

**What Worked:**
✅ NoAns accuracy jumped from 13% → 78%  
✅ Gate stopped predicting YES for everything  
✅ Windowing + grounding + shrink-to-span pipeline is solid  
✅ No hallucinations - strict extractive enforcement

**What Didn't Work:**
❌ HasAns dropped to ~26% (too conservative)  
❌ Gate + verifier rejecting many correct answers  
❌ Runtime still ~10 minutes for 50 samples (too slow)  
❌ Verifier is expensive: 2 forward passes per example, NOT batched

**Key Code Sections:**

*Windowing with keyword scoring:*
```python
def _top_k_windows(tokenizer, context, question, max_tokens, stride, top_k):
    # Extract keywords from question (filter stopwords)
    keys = _keywords(question)
    
    # Slide windows and score by keyword overlap
    for start in range(0, len(ids), step):
        chunk = tokenizer.decode(ids[start:end])
        score = _overlap_score(chunk, keys)  # Count keyword occurrences
        windows.append((score, start, chunk))
    
    # Return top-k highest scoring windows
    windows.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    return [w[2] for w in windows[:top_k]]
```

*Grounding gate:*
```python
def _finalize_answer(answer_text, context, allow_shrink):
    if _looks_like_no_answer(answer_text):
        return NO_ANSWER_MARKER
    
    # Try exact/fuzzy/regex grounding
    grounded = _ground_exact_or_fuzzy(answer_text, context)
    if grounded is not None:
        return grounded
    
    # Try shrink-to-span (n-gram search)
    if allow_shrink:
        shrunk = _shrink_to_span(answer_text, context)
        if shrunk is not None:
            return shrunk
    
    return NO_ANSWER_MARKER  # Default to NO ANSWER if can't ground
```

*Verifier (expensive):*
```python
def _verify_answer_supported(tokenizer, model, device, question, context, answer, max_length):
    # Build verification prompt
    msgs = [
        {"role": "system", "content": "You are a strict QA verifier. Reply ONLY YES or NO."},
        {"role": "user", "content": f"QUESTION:\n{question}\n\nCONTEXT:\n{context}\n\nPROPOSED ANSWER:\n{answer}\n\nIs the proposed answer fully supported by the context for this question? YES or NO: "}
    ]
    
    # Compute YES vs NO logprob
    yes_lp = _completion_logprob_sum(model, input_ids, attn, _YES_TOKEN_IDS, ...)
    no_lp = _completion_logprob_sum(model, input_ids, attn, _NO_TOKEN_IDS, ...)
    
    return (yes_lp - no_lp).item() > VERIFY_MARGIN
```

---

## 📊 Performance Comparison

| Metric | Trial 1 (Next-Token) | Trial 2 (Completion) | Change |
|--------|---------------------|---------------------|--------|
| **Gate YES%** | 100.0% | 62.0% | ✅ -38% |
| **Exact Match** | 36.0 | 50.0 | ✅ +14.0 |
| **F1 Score** | 39.667 | 51.0 | ✅ +11.3 |
| **HasAns_exact** | 55.556 | 25.926 | ❌ -29.6 |
| **NoAns_exact** | 13.043 | 78.261 | ✅ +65.2 |
| **Runtime (50 samples)** | 618.79s | 600.94s | ≈ same |

---

## 🔑 Key Lessons Learned

### 1. Tokenization Matters (Llama-Specific)
- Llama tokenizers encode `"YES"` vs `" YES"` (with leading space) differently
- Single-token assumptions can break the gate completely
- Must use `tokenizer.encode()` and handle multi-token completions

### 2. Completion Logprob Sum is Expensive
- Current implementation: 2 forward passes per batch (YES + NO) for classification
- Verifier: 2 forward passes **per example** (not batched!)
- Major contributor to ~600s runtime

### 3. Trade-off: NoAns vs HasAns
- Strong NoAns improvement (78%) came at cost of HasAns (26%)
- Gate + verifier too conservative
- Need better threshold calibration

### 4. What Actually Works
✅ Windowing by keyword overlap keeps relevant context  
✅ Strict grounding gate prevents hallucinations  
✅ Shrink-to-span helps align paraphrased answers  
✅ Two-stage pipeline (when calibrated) can improve NoAns

---

## 🚧 Current Code State

**Active Implementation:** Trial 2 (Multi-token completion logprob)

**Important Configuration Parameters:**
```python
# Batch sizes
BATCH_SIZE_CLASSIFY = 24   # Classification (no generation)
BATCH_SIZE_ANSWER = 4      # Answer generation

# Token limits
MAX_NEW_TOKENS_ANSWER = 24
MAX_CTX_TOKENS_CLASSIFY = 256
MAX_CTX_TOKENS_ANSWER = 900
MAX_PROMPT_TOKENS_CAP = 1024

# Thresholds
ANSWERABLE_LOGIT_MARGIN = -0.5  # Gate threshold (logprob units)
VERIFY_MARGIN = 0.3              # Verifier threshold

# Windowing
WINDOW_STRIDE = 128
TOPK_CLASSIFY_WINDOWS = 1
TOPK_ANSWER_WINDOWS = 2
```

**Pipeline Flow:**
```
1. Load model once (GPU, float16, left-padding)
2. For each sample:
   a. Build classify window (top-1, 256 tokens)
   b. Compute YES/NO logprob sums
   c. Gate decision: answerable if (yes_lp - no_lp) > -0.5
3. For answerable samples:
   a. Try answer window #1 (top-1, 900 tokens)
   b. Generate answer (max 24 new tokens)
   c. Ground/shrink to context span
   d. Verify with YES/NO logprob
   e. If failed, retry with window #2
4. Output final answer or NO ANSWER
```

**Code Structure:**
- Lines 1-410: Commented-out earlier versions
- Lines 412-664: Model loading, token resolution, utilities
- Lines 667-735: Prompt building and context truncation
- Lines 737-844: Grounding and answer finalization
- Lines 847-987: Answerability gate (batched)
- Lines 994-1048: Answer generation (batched)
- Lines 1055-1248: Main `squad_qa()` function
- Lines 1255-1274: Entry point

---

## ⚠️ Known Issues

### Critical Issues:
1. **HasAns too low (25.926%)** - Gate rejecting too many answerable questions
2. **Runtime too high (~600s for 50)** - Verifier not batched, expensive logprob computation
3. **Verifier overhead** - 2 forward passes per example, sequential

### Technical Debt:
1. Multiple commented-out code versions (lines 1-410) - needs cleanup
2. Verifier not batched with answer generation
3. No systematic threshold tuning - margins chosen by guessing

---

## 🎯 Recommended Next Steps

### Priority 1: Fix YES/NO Tokenization (Revisit Trial 1 Correctly)
- Encode with leading space: `" YES"` and `" NO"`
- Verify single-token encoding
- Use single forward pass (faster than completion logprob sum)
- Tune threshold empirically on dev set

### Priority 2: Reduce Verifier Cost
Options:
- Disable verifier temporarily (rely on grounding gate only)
- Batch verifier prompts
- Only verify when answer was "shrunk" (paraphrased)
- Replace with single-pass next-token verifier

### Priority 3: Improve HasAns Without Killing NoAns
- Lower `ANSWERABLE_LOGIT_MARGIN` (try -0.8, -1.0)
- Increase `MAX_CTX_TOKENS_ANSWER` if VRAM allows
- Allow `TOPK_ANSWER_WINDOWS = 3` for edge cases

### Priority 4: Systematic Threshold Tuning
- Log `yes_score - no_score` for each sample
- Analyze distribution for HasAns vs NoAns
- Choose threshold maximizing F1 or balanced accuracy

---

## 📈 Experiment Log

### EXP-1: Next-token logprob gate, single-token IDs
**Status:** ❌ FAILED  
**Config:** margin=0.0, single-token YES/NO  
**Results:**
- Gate: YES=50/50 (100%)
- exact=36.0, f1=39.667
- HasAns_exact=55.556, NoAns_exact=13.043
- Runtime: 618.79s

### EXP-2: Completion logprob sum, multi-token, verifier enabled
**Status:** ⚠️ PARTIAL SUCCESS  
**Config:** margin=-0.5, verify_margin=0.3, 2-window retry  
**Results:**
- Gate: YES=31/50 (62%)
- exact=50.0, f1=51.0
- HasAns_exact=25.926, NoAns_exact=78.261
- Runtime: 600.94s

---

## 💡 Insights for Report

### What Worked:
- Two-stage pipeline with answerability gating
- Keyword-based windowing for context relevance
- Strict grounding enforcement (exact/fuzzy/regex/shrink)
- Multi-token completion logprob for YES/NO classification

### What Didn't Work:
- Single-token next-logprob gate (tokenization issues)
- Untuned thresholds (too conservative)
- Expensive per-example verifier (not batched)

### Trade-offs:
- **NoAns vs HasAns:** Achieved 78% NoAns but sacrificed HasAns (26%)
- **Speed vs Accuracy:** Verifier improves precision but adds ~50% overhead
- **Context size vs Relevance:** Windowing helps but may miss distant answers

### Easy vs Difficult Cases:
- **Easy NoAns:** Questions with clear topic mismatch to context
- **Easy HasAns:** Direct factual questions with exact span in context
- **Difficult NoAns:** Questions about context topic but answer not present
- **Difficult HasAns:** Paraphrased answers, multi-hop reasoning, long contexts

---

## 📝 Summary

Gideon attempted to solve the SQuAD 2.0 unanswerable detection task through **3 planning iterations** and **2 major experimental trials**. The core challenge was balancing NoAns (don't hallucinate) with HasAns (don't over-reject).

**Trial 1 failed catastrophically** due to tokenization issues with single-token YES/NO encoding, resulting in a gate that always predicted "answerable" (100% YES rate, 13% NoAns accuracy).

**Trial 2 achieved the primary objective** of strong NoAns detection (78% accuracy) through multi-token completion logprob gating and strict grounding, but **over-corrected** and damaged HasAns performance (26% accuracy). The implementation includes sophisticated windowing, grounding gates, and answer verification, but suffers from high runtime (~10 min for 50 samples) due to unbatched verifier calls.

**Both trials failed to meet the balanced performance requirement**, though Trial 2 demonstrates a viable architecture that needs calibration. The next teammate should focus on threshold tuning, verifier optimization, and recovering HasAns performance without sacrificing the NoAns gains.

---

**Status:** 🟡 In Progress - Architecture viable, needs optimization  
**Blocking Issues:** HasAns too low, runtime too high  
**Next Owner:** Should prioritize threshold tuning and verifier batching
