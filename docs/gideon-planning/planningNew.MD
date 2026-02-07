# NLP Final Project Plan (SQuAD 2.0 + Llama 3.2 3B) — Consolidated Experiment Log

This is the **handoff planning.md** for our SQuAD 2.0 QA project using **`meta-llama/Llama-3.2-3B-Instruct`**.  
It captures: **the original plan**, **every major code version we tried**, **what worked / didn’t**, **terminal metrics**, and **next experiments**.

Goal remains: **high QA performance** while **never hallucinating** — if the answer is not explicitly grounded in the context, output **`NO ANSWER`**.

---

## 0) Project Summary

We build a Question Answering system for **SQuAD 2.0**:
- Input: `(context, question)` (from CSV)
- Output: either:
  - an extractive answer span copied from context, or
  - the exact marker: **`NO ANSWER`**

The grader runs `main.py` as-is. Our solution must:
- implement `squad_qa(data_filename)` and produce `*-results.csv`
- add column **`final answer`**
- keep outputs grounded (extractive)

Primary objective: **strong NoAns** (don’t hallucinate).  
Secondary objective: **preserve HasAns** (don’t say NO ANSWER too often).

---

## 1) Repo Contract / Constraints

### Hard constraints
- Model: `meta-llama/Llama-3.2-3B-Instruct`
- Output CSV must be: `<input>-results.csv`
- Column must be: `final answer`
- No-answer marker must match exactly: `NO ANSWER`

### Operational constraints
- Windows + GPU (RTX 4050 6GB)
- Reasonable runtime for grading sample (~50 rows)

---

## 2) Original Baseline Plan (from prior planning.md)

Core principles we committed to:
1. **Never hallucinate**: if output can’t be grounded to context → `NO ANSWER`
2. **Extractive**: return shortest span copied from context
3. **Runtime**: load model once, GPU, batching, small `max_new_tokens`
4. Add **post-processing grounding gate**:
   - exact substring match
   - case-insensitive match
   - regex-flex match by word sequence
   - else `NO ANSWER`

This plan worked conceptually, then we experimented with stronger gating.

---

## 3) Architecture We Implemented (the “two-stage” pipeline)

### Stage A — Answerability gating (YES/NO)
We added an “answerable?” step before generating answers to improve NoAns.

The design:
- Build a prompt: question + (truncated / windowed) context
- Ask model to output **exactly** YES or NO
- Decide answerable vs not using **logprob** comparison (YES vs NO)

### Stage B — Answer generation (only for gated YES)
- For gated-YES rows, ask model for extractive answer
- Apply strict post-processing:
  - clean first line
  - grounding check (exact / fuzzy / regex)
  - optional shrink-to-span (n-gram search inside context)
  - otherwise `NO ANSWER`

### Optional Stage C — “Verifier” (YES/NO on proposed answer)
We added a second check:
- question + context + proposed answer
- ask: “Is it fully supported?” (YES/NO)
- accept only if YES logprob beats NO by margin

---

## 4) Context Handling Experiments

To reduce prompt length and improve relevance, we used **windowing**:

- `_top_k_windows()`:
  - tokenize full context into ids
  - slide windows of `max_tokens` with `stride`
  - score each window by keyword overlap with question
  - choose top-k windows:
    - classify: `TOPK_CLASSIFY_WINDOWS = 1`
    - answer: `TOPK_ANSWER_WINDOWS = 2`
- Answer stage tries window #1 first, then retries remaining failures with window #2.

Current knobs (in code):
- `MAX_CTX_TOKENS_CLASSIFY = 256`
- `MAX_CTX_TOKENS_ANSWER = 900`
- `WINDOW_STRIDE = 128`
- `MAX_PROMPT_TOKENS_CAP = 1024`

---

## 5) Code Versions We Tried + Results

### Version 1 — “Single-token next-logprob gate” (FAILED badly)
**What changed**
- Answerability gate used **next-token logprob**:
  - resolve single token ids: `_YES_TOKEN_ID`, `_NO_TOKEN_ID`
  - compute `yes_lp - no_lp` from last logits
- `ANSWERABLE_LOGIT_MARGIN = 0.0`
- Result: the gate said **YES for everything** → terrible NoAns.

**Terminal run**


[squad_qa] rows=50 device=cuda bs_cls=24 bs_ans=4 prompt_cap=1024
[classify] starting...
[squad_qa] answerable_gate: YES=50 / 50 (100.0%)
...
('exact', 36.0)
('f1', 39.667)
('HasAns_exact', 55.556) # OK-ish
('NoAns_exact', 13.043) # catastrophic
time: 618.79 sec



**Why it likely failed**
- Tokenization mismatch for YES/NO (leading-space tokens matter on Llama tokenizers).
- Prompt formatting may cause model to prefer “YES” by default.
- Even small logit bias makes “YES” dominate without calibration.
- Gate became useless → answered unanswerable questions → NoAns collapsed.

**Decision**
- Abandon this approach *as implemented* (but we may revisit with correct token ids + threshold tuning).

---

### Version 2 — “Multi-token completion logprob gate + verifier” (WORKED PARTIALLY)
This is the **current reverted code** you pasted.

**What changed**
- Instead of single-token next-logprob, we compute logprob for the *full completion*:
  - `_YES_TOKEN_IDS = tokenizer.encode("YES")`
  - `_NO_TOKEN_IDS  = tokenizer.encode("NO")`
  - `_completion_logprob_sum()` appends completion ids and sums token logprobs.
- Gate threshold set to:
  - `ANSWERABLE_LOGIT_MARGIN = -0.5` (more permissive than 0.0)
- Kept:
  - windowing (top-k)
  - strict post-processing + shrink-to-span
  - verifier step using the same completion-logprob-sum (YES/NO)

**Terminal run**


[squad_qa] rows=50 device=cuda bs_cls=24 bs_ans=4 prompt_cap=1024
[classify] starting...
[squad_qa] answerable_gate: YES=31 / 50 (62.0%)
...
('exact', 50.0)
('f1', 51.0)
('HasAns_exact', 25.926) # bad (too many false NO ANSWER)
('NoAns_exact', 78.261) # strong improvement
time: 600.94 sec



**Interpretation**
- We achieved the main “no hallucination” direction:
  - **NoAns jumped to ~78%**
- But we over-shot on conservativeness:
  - HasAns dropped hard (~26% exact)
  - Gate + verifier likely rejecting many answerable questions.

**What “worked” here**
- Windowing + grounding + shrink-to-span is solid.
- The gate finally stopped saying YES to everything.
- NoAns performance improved a lot.

**What “didn’t work”**
- Gate calibration is off (too many false negatives).
- Verifier is expensive and may be rejecting correct spans due to strictness / prompt issues.
- Runtime is still ~10 minutes for 50 rows (too slow for comfort).

---

## 6) Key Lessons Learned

### 6.1 YES/NO tokenization matters a lot (Llama-specific)
- Llama tokenizers often encode `" YES"` differently than `"YES"`.
- If we choose the wrong token ids, the gate becomes meaningless (Version 1).

### 6.2 Completion-logprob-sum is expensive
- `_completion_logprob_sum()` runs a full forward pass per completion set.
- Current gating uses:
  - 2 forward passes per batch (YES + NO)
- Verifier runs:
  - 2 forward passes *per example* (YES + NO), and currently **not batched**
This heavily contributes to ~600s runtime.

### 6.3 We currently trade HasAns for NoAns too aggressively
- Good NoAns is great, but we must recover HasAns by:
  - better threshold tuning
  - better YES/NO token selection
  - relaxing verifier usage

---

## 7) Current Code Snapshot (what’s in the reverted version)

### Important knobs
- `ANSWERABLE_LOGIT_MARGIN = -0.5`
- `VERIFY_MARGIN = 0.3`
- `MAX_PROMPT_TOKENS_CAP = 1024`
- `MAX_CTX_TOKENS_CLASSIFY = 256`
- `MAX_CTX_TOKENS_ANSWER = 900`
- `TOPK_ANSWER_WINDOWS = 2`
- `BATCH_SIZE_CLASSIFY = 24`
- `BATCH_SIZE_ANSWER = 4`
- `MAX_NEW_TOKENS_ANSWER = 24`

### Pipeline summary
1. Build classify window → prompt → gate YES/NO via completion logprob sum
2. For YES rows:
   - generate answer from window #1
   - post-process (ground/shrink)
   - verify YES/NO (completion logprob sum)
   - retry remaining failures with window #2
3. Output `final answer`

---

## 8) What We Tried That Didn’t Work (explicit list)

1. **Single-token next-logprob YES/NO gate** → gate returned **YES=100%**, NoAns collapsed.
2. **Setting gate margin at 0.0 (with Version 1)** → did not help; still YES=100%.
3. **Verifier + completion-logprob-sum (current)** improves precision but is:
   - very slow
   - possibly too strict (rejects correct answers)

---

## 9) What Worked (even if only partially)

1. **Windowing by keyword overlap** helps keep relevant context.
2. **Strict grounding gate + shrink-to-span** reduces hallucinations and enforces extractive outputs.
3. **Answerability gating** (when not broken) can substantially improve **NoAns**.

---

## 10) Recommended Next Experiments (for teammate)

### A) Fix YES/NO token IDs properly (revisit Version 1, but correctly)
Goal: keep the *speed* of single forward pass while avoiding “YES always”.

1. Resolve IDs using leading space first:
   - encode `" YES"` and `" NO"` and ensure they are **single tokens**
2. Compute YES/NO from the **same logits** (one forward pass), like:
   - `logp = log_softmax(logits_last)`
   - `diff = logp[YES] - logp[NO]`
3. Collect diffs on a dev sample and tune threshold.

Why: fastest + easiest to calibrate.

---

### B) Tune thresholds systematically (stop guessing)
Add a debug mode that logs:
- `diff = yes_score - no_score` for each row
- whether it was HasAns/NoAns (from dataset column if present, or by comparing to gold if available)
Then choose threshold maximizing `best_f1` or balanced score.

---

### C) Reduce verifier cost (major runtime win)
Current verifier is per-example, 2 forward passes each.

Options:
1. **Disable verifier** temporarily; rely on grounding gate.
2. Verify only when answer was “shrunk” (i.e., model paraphrased).
3. Batch verifier prompts per window (same as generation batching).
4. Replace completion-logprob-sum verifier with next-token single-pass verifier.

---

### D) Improve HasAns without killing NoAns
If NoAns is good but HasAns is low:
- make gate more permissive:
  - lower `ANSWERABLE_LOGIT_MARGIN` further (e.g., -0.8, -1.0) and measure
- increase answer context window size slightly (if VRAM allows)
- allow `TOPK_ANSWER_WINDOWS = 3` only for cases where window #1/#2 failed grounding

---

## 11) Execution Notes (Windows / HF)

Run:
- `python .\main.py`

Expect output:
- `...-sample.csv`
- `...-sample-results.csv` with same row count
- printed evaluation block:
  - `exact`, `f1`, `HasAns_*`, `NoAns_*`, `best_*`

---

## 12) Current Status Summary

- Best NoAns so far: **Version 2 (completion logprob gate)**  
  - `NoAns_exact ≈ 78.261` (on sample=50)
- But HasAns is too low:
  - `HasAns_exact ≈ 25.926`
- Runtime is still high:
  - ~600 seconds for 50

Immediate next priority:
1. Fix YES/NO tokenization (leading space tokens) and move back to **single-pass** logprob gating.
2. Tune gate threshold empirically.
3. Reduce verifier overhead (batch or remove).

---

## 13) Experiment Log (copy/paste friendly)

### EXP-1 (FAILED): next-token logprob gate, single-token ids
- Gate: YES=50/50 (100%)
- exact=36.0, f1=39.667
- HasAns_exact=55.556
- NoAns_exact=13.043
- time=618.79 sec

### EXP-2 (PARTIAL SUCCESS): completion logprob sum (multi-token), margin=-0.5, verifier enabled
- Gate: YES=31/50 (62%)
- exact=50.0, f1=51.0
- HasAns_exact=25.926
- NoAns_exact=78.261
- time=600.94 sec
