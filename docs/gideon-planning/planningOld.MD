# NLP Final Project Plan (SQuAD 2.0 + Llama 3.2 3B)

This document is the shared, step-by-step plan for implementing the project.  
Goal: **high QA performance** while **never hallucinating** — if the answer is not explicitly grounded in the context, return **`NO ANSWER`**.

---

## 0) Project Summary

We are building a Question Answering system for **SQuAD 2.0**:
- Input: **(context, question)**
- Output: either:
  - an **extractive answer** (copied from the context), or
  - **`NO ANSWER`** when the context does not contain the answer.

The grader runs `main()` as-is. Our solution must work through the existing entrypoint and file outputs.

**Primary objective:** improve **NoAns** (unanswerable) accuracy substantially.  
**Secondary objective:** maintain strong HasAns performance.  
**Operational objective:** keep runtime reasonable, especially on grading samples (~50).

---

## 1) Key Constraints & Success Criteria

### Hard constraints
- Use model: `meta-llama/Llama-3.2-3B-Instruct`.
- Do not stack with another LLM.
- Produce a results CSV with column **`final answer`**.
- Output file naming must follow: `*-sample.csv` → `*-sample-results.csv` (same prefix).
- `NO ANSWER` must match the required marker exactly: `NO ANSWER`.

### What “good” looks like
- **NoAns metrics** improve significantly without destroying HasAns.
- Predictions are **grounded** in context (extractive).
- Execution completes reliably on Windows + GPU.

---

## 2) Repo and Files

### Important files
- `main.py`
  - Contains `main()` (sampling + calling `squad_qa()` + evaluation).
  - We implement `squad_qa(data_filename)` and helper functions.
- `utils/query_model.py`
  - Sanity check that model downloads and runs.
- `utils/evaluate_results.py`
  - Evaluates results using SQuAD v2 metric; expects `final answer` column.
- `config.json`
  - `data`: path to dataset CSV
  - `sample_for_solution`: we use 1000 for development runs
  - `sample_for_grading`: grader typically uses 50 (runtime check)

### Output files
- `data/squad2.0-dev-1000-sample.csv`
- `data/squad2.0-dev-1000-sample-results.csv`  ← must have 1000 rows when using solution sample size

---

## 3) Execution & Verification Commands

### Environment checks
- Create venv and activate (Windows PowerShell):
  - `py -3.13 -m venv .venv`
  - `.\.venv\Scripts\Activate.ps1`

### HF auth and model access
- Login:
  - `.\.venv\Scripts\hf.exe auth login`
- Verify active user:
  - `.\.venv\Scripts\hf.exe auth whoami`

### Smoke test the model
- `python .\utils\query_model.py`

### Run the project entrypoint
- `python .\main.py`

### Verify sample/results sizes
- `python -c "import pandas as pd; print(pd.read_csv('data/squad2.0-dev-1000-sample.csv').shape)"`
- `python -c "import pandas as pd; print(pd.read_csv('data/squad2.0-dev-1000-sample-results.csv').shape)"`

Expected:
- sample: `(1000, ...)`
- results: `(1000, ...)` after implementation is complete

---

## 4) Design Principles (What we optimize for)

### 4.1 “No hallucinations” is the top priority
We **only** return an answer if we can prove it is grounded in the context.

**Grounding rule:**  
If the model output cannot be matched back to a substring/span in the context with high confidence → output **`NO ANSWER`**.

### 4.2 Keep answers extractive
SQuAD v2 exact match and F1 reward answers that match the gold span.

So even for answerable questions:
- Keep responses short.
- Prefer exact spans.
- If the model paraphrases: attempt to align back to an exact span. If impossible: choose `NO ANSWER`.

### 4.3 Runtime matters
- Load model/tokenizer once.
- Use GPU.
- Use batching.
- Use deterministic decoding (`do_sample=False`).
- Keep `max_new_tokens` low (answers are short).
- Avoid multi-pass calls unless we can justify the gain.

---

## 5) Implementation Plan (Ordered Steps)

### Step 1 — Stabilize the pipeline contract (must-pass)
**Goal:** `main.py` run produces a results file with correct row count and column.

Tasks:
1. Ensure `main()` remains runnable and unchanged in behavior (sampling + evaluation).
2. Implement `squad_qa(data_filename)` so it:
   - reads `data_filename` (the sample CSV produced by main)
   - generates `final answer` for each row
   - writes `out_filename = data_filename.replace('.csv', '-results.csv')`
   - returns `out_filename`

Verification:
- Running `python main.py` prints metrics (total = sample size).
- Results CSV row count equals sample row count.

---

### Step 2 — Model loading & device placement (fast + stable)
**Goal:** eliminate slow CPU-offload behavior and batching issues.

Tasks:
1. Load model with dtype appropriate to device (`float16` on CUDA).
2. Place model fully on GPU if available (avoid `device_map="auto"` offload).
3. Set tokenizer padding correctly for decoder-only model:
   - `tokenizer.padding_side = "left"`
   - ensure `pad_token_id = eos_token_id` if missing

Verification:
- No repeated “right-padding detected” spam.
- No “parameters on meta device because they were offloaded” slowdowns.
- Throughput is stable and predictable.

---

### Step 3 — Prompt contract (force answerable vs unanswerable)
**Goal:** consistent outputs that are easy to parse.

Prompt rules:
- Use only the given context.
- If not answerable: output exactly `NO ANSWER`.
- If answerable: output the shortest exact answer span copied from context.
- Output must be one line (no explanations).

Verification:
- Generated text is short.
- Many outputs are either a short span or `NO ANSWER`.

---

### Step 4 — Grounding gate (the core NoAns improvement)
**Goal:** reject hallucinations and enforce extractive answers.

Algorithm (post-processing):
1. Clean model output (strip, first line).
2. If it looks like refusal/uncertainty → `NO ANSWER`.
3. Try grounding:
   - exact substring match
   - case-insensitive match (return original slice)
   - flexible word-sequence regex match (handles punctuation/spaces)
4. If no grounding match → `NO ANSWER`.

Verification:
- No answers that aren’t in context.
- NoAns accuracy improves.

---

### Step 5 — Performance optimization
**Goal:** keep 50-sample grading runs fast; make 1000 runs feasible.

Levers:
- Batch size (GPU): start 4, adjust based on VRAM.
- `max_new_tokens`: start 32 (can reduce to 16–24 if stable).
- Truncate context to fit token budget:
  - preserve the question + instructions
  - cap context tokens based on model max input length
- Use `torch.inference_mode()` and `use_cache=True`.

Verification:
- 50-sample run completes quickly.
- 1000-sample run completes without crashes or huge slowdowns.

---

### Step 6 — Evaluation loop and error analysis
**Goal:** systematically improve, not guess.

Process:
1. Run on the 1000 dev subset and record metrics:
   - exact / f1
   - HasAns_exact / HasAns_f1
   - NoAns_exact / NoAns_f1
2. Inspect failures:
   - false NO ANSWER on answerable questions (too strict grounding)
   - false answered on unanswerable questions (prompt needs tightening)
   - paraphrase not aligning to context
3. Tune:
   - prompt wording
   - grounding tolerance (regex rules)
   - max tokens / truncation strategy

Artifacts to keep:
- a simple experiment log (date, change, metrics, runtime)
- a set of example failures for the report

---

### Step 7 — Final deliverables
- `main.py` with working solution.
- `data/squad2.0-dev-1000-sample-results.csv` (1000 rows).
- 3–4 page report:
  - approach overview
  - NoAns strategy (grounding gate)
  - metrics comparison (before/after)
  - runtime estimate
  - limitations and future work

---

## 6) Common Pitfalls & How We Avoid Them

### Pitfall: “Total=50” even when sample_for_solution=1000
Cause: results CSV not regenerated; evaluator reuses old file.  
Fix: `squad_qa()` must actually write results matching the input sample.

### Pitfall: Gated model 403/401 errors
Cause: HF token not logged in or model access not granted.  
Fix: ensure `hf auth whoami` works and access is accepted on model page.

### Pitfall: Slow generation with CPU offload / meta device
Cause: `device_map="auto"` offloads parameters to CPU and swaps constantly.  
Fix: load model fully on GPU and avoid offload.

### Pitfall: Decoder-only right padding warning spam
Cause: tokenizer default `padding_side="right"` with batching.  
Fix: set `tokenizer.padding_side="left"`.

---

## 7) Current Status

✅ Environment:
- venv on Python 3.13.7
- Hugging Face auth works (`hf auth whoami` OK)
- `utils/query_model.py` runs and loads model

✅ Entry point:
- `main.py` baseline runs (previously, before implementing `squad_qa()`)

🟦 Next action:
- Implement Step 1–4 in `main.py` cleanly (pipeline + prompt + grounding gate)
- Confirm results CSV is 1000 rows when `sample_for_solution=1000`

---

## 8) Handoff Notes (If one of us stops mid-way)

When resuming:
1. Run `python main.py` and check:
   - does it print progress?
   - does it produce `*-sample-results.csv`?
2. Check file shapes:
   - sample should be 1000 rows
   - results should match sample row count
3. If it crashes:
   - note whether it is VRAM (OOM) → reduce batch size
   - note whether it is offload warnings → ensure no `device_map="auto"`
4. Commit small, incremental changes with clear messages:
   - “Implement squad_qa pipeline”
   - “Add grounding gate”
   - “Fix tokenizer left padding”
   - “Tune prompt + max_new_tokens”

---
