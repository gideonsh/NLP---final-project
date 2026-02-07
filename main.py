import json
# import pandas as pd
import time
# import torch
# torch.set_default_device('cpu')

# from transformers import AutoModelForCausalLM, AutoTokenizer
from utils.evaluate_results import NO_ANSWER_MARKER, evaluate_results


# model_name = 'meta-llama/Llama-3.2-3B-Instruct'
# tokenizer = AutoTokenizer.from_pretrained(model_name, token=True)
# model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16, token=True)
# model.config.pad_token_id = tokenizer.eos_token_id
# tokenizer.pad_token_id = tokenizer.eos_token_id


# def squad_qa(data_filename):

#     # todo: implement this function, design your solution and document properly

#     # todo: you will need to sign up for huggingface and visit https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct to get access
#     # todo: squad2.0 dataset - https://huggingface.co/datasets/rajpurkar/squad_v2


#     out_filename = data_filename.replace('.csv', '-results.csv')
#     print(f'final answers recorded into {out_filename}')
#     return out_filename


# if __name__ == '__main__':
#     start_time = time.time()

#     with open('config.json', 'r') as json_file:
#         config = json.load(json_file)

#     data = pd.read_csv(config['data'])
#     sample = data.sample(n=config['sample_for_solution'])  # for grading will be replaced with 'sample_for_grading'
#     sample_filename = config['data'].replace('.csv', '-sample.csv')
#     sample.to_csv(sample_filename, index=False)

#     out_filename = squad_qa(sample_filename)  # todo: the function you implement

#     eval_out = evaluate_results(out_filename, final_answer_column='final answer')
#     eval_out_list = [str((k, round(v, 3))) for (k, v) in eval_out.items()]
#     print('\n'.join(eval_out_list))

#     elapsed_time = time.time() - start_time
#     print(f"time: {elapsed_time: .2f} sec")


################################################################################################################

# import os
# import re
# from typing import List, Tuple, Optional

# import pandas as pd
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer

# from utils.evaluate_results import NO_ANSWER_MARKER

# MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct"

# # Globals (lazy-loaded once)
# _TOKENIZER: Optional[AutoTokenizer] = None
# _MODEL: Optional[AutoModelForCausalLM] = None
# _DEVICE: Optional[torch.device] = None
# _MAX_INPUT_TOKENS: Optional[int] = None


# # ----------------------------
# # Model / tokenizer utilities
# # ----------------------------

# def _get_device() -> torch.device:
#     return torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")


# def _infer_max_input_tokens(model, tokenizer) -> int:
#     """
#     Determine a safe max input length for generation.
#     Prefer model.config.max_position_embeddings; fall back to tokenizer.model_max_length.
#     Cap overly-large values to keep runtime sane.
#     """
#     max_pos = getattr(model.config, "max_position_embeddings", None)
#     if isinstance(max_pos, int) and max_pos > 0:
#         # If the config is huge (some tokenizers report enormous lengths),
#         # cap to a reasonable limit for throughput.
#         return min(max_pos, 8192)

#     tmax = getattr(tokenizer, "model_max_length", None)
#     if isinstance(tmax, int) and 0 < tmax < 10**6:
#         return min(tmax, 8192)

#     return 4096


# def _load_model_once() -> Tuple[AutoTokenizer, AutoModelForCausalLM, torch.device, int]:
#     global _TOKENIZER, _MODEL, _DEVICE, _MAX_INPUT_TOKENS

#     if _TOKENIZER is not None and _MODEL is not None and _DEVICE is not None and _MAX_INPUT_TOKENS is not None:
#         return _TOKENIZER, _MODEL, _DEVICE, _MAX_INPUT_TOKENS

#     device = _get_device()

#     if device.type == "cuda":
#         torch.backends.cuda.matmul.allow_tf32 = True

#     tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=True)
#     if tokenizer.pad_token_id is None:
#         tokenizer.pad_token_id = tokenizer.eos_token_id

#     # IMPORTANT for decoder-only models with batching
#     tokenizer.padding_side = "left"

#     dtype = torch.float16 if device.type == "cuda" else torch.float32

#     # IMPORTANT: do NOT use device_map="auto" here (it offloads to CPU and becomes super slow)
#     model = AutoModelForCausalLM.from_pretrained(
#         MODEL_NAME,
#         token=True,
#         dtype=dtype,
#         low_cpu_mem_usage=True,
#     )

#     model.to(device)
#     model.eval()
#     model.config.pad_token_id = tokenizer.pad_token_id

#     max_input_tokens = _infer_max_input_tokens(model, tokenizer)

#     _TOKENIZER, _MODEL, _DEVICE, _MAX_INPUT_TOKENS = tokenizer, model, device, max_input_tokens
#     return tokenizer, model, device, max_input_tokens



# # ----------------------------
# # Prompting and parsing
# # ----------------------------

# def _system_prompt() -> str:
#     return (
#         "You are a question answering assistant for SQuAD2.0.\n"
#         "Use ONLY the given CONTEXT.\n"
#         f"If the answer is not explicitly in the CONTEXT, reply exactly: {NO_ANSWER_MARKER}\n"
#         "If answerable, reply with the shortest exact answer span copied verbatim from the CONTEXT.\n"
#         "Reply with ONE line and nothing else."
#     )


# def _build_messages(context: str, question: str) -> List[dict]:
#     user = (
#         "CONTEXT:\n"
#         f"{context}\n\n"
#         "QUESTION:\n"
#         f"{question}\n\n"
#         "ANSWER:"
#     )
#     return [
#         {"role": "system", "content": _system_prompt()},
#         {"role": "user", "content": user},
#     ]


# def _truncate_context_to_fit(tokenizer, model, context: str, question: str, max_input_tokens: int, max_new_tokens: int) -> str:
#     """
#     Token-budget the context so we don't truncate away the question/instructions.
#     We compute overhead for the chat template with empty context, then allocate
#     remaining tokens to context.
#     """
#     # Build overhead prompt with empty context to estimate budget usage
#     overhead_msgs = _build_messages("", question)
#     overhead_ids = tokenizer.apply_chat_template(
#         overhead_msgs,
#         tokenize=True,
#         add_generation_prompt=True,
#     )
#     overhead_len = len(overhead_ids)

#     # Leave a small safety margin
#     budget = max_input_tokens - max_new_tokens - overhead_len - 8
#     if budget <= 32:
#         # Extremely tight budget; just keep a tiny prefix
#         return context[:500]

#     ctx_ids = tokenizer(context, add_special_tokens=False).input_ids
#     if len(ctx_ids) <= budget:
#         return context

#     ctx_ids = ctx_ids[:budget]
#     return tokenizer.decode(ctx_ids, skip_special_tokens=True)


# def _clean_model_text(text: str) -> str:
#     """
#     Clean the model output to a single-line candidate answer.
#     """
#     if text is None:
#         return ""
#     text = text.strip()

#     # Keep only the first non-empty line
#     lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
#     if not lines:
#         return ""
#     text = lines[0]

#     # Remove wrapping quotes/backticks
#     text = text.strip(" \t\r\n`\"'")

#     return text.strip()


# def _is_no_answer(text: str) -> bool:
#     if not text:
#         return True
#     t = text.strip().lower()
#     if t == NO_ANSWER_MARKER.lower():
#         return True
#     # Sometimes the model adds punctuation
#     if t.startswith(NO_ANSWER_MARKER.lower()):
#         return True
#     # Common refusal phrasing => treat as no answer
#     if any(p in t for p in ["not mentioned", "cannot be determined", "insufficient information", "no information"]):
#         return True
#     return False


# def _ground_to_context(answer: str, context: str) -> str:
#     """
#     Strong grounding gate:
#     - Accept the answer only if we can find it in the context (exact / case-insensitive / regex-flex).
#     - Otherwise return NO ANSWER.
#     """
#     answer = _clean_model_text(answer)
#     if _is_no_answer(answer):
#         return NO_ANSWER_MARKER

#     if context is None:
#         return NO_ANSWER_MARKER

#     ctx = str(context)
#     if not ctx.strip():
#         return NO_ANSWER_MARKER

#     # 1) Exact substring
#     idx = ctx.find(answer)
#     if idx >= 0:
#         return answer

#     # 2) Case-insensitive substring (return original slice)
#     low_ctx = ctx.lower()
#     low_ans = answer.lower()
#     idx = low_ctx.find(low_ans)
#     if idx >= 0:
#         return ctx[idx: idx + len(answer)]

#     # 3) Flexible regex based on word sequence (handles multiple spaces / punctuation)
#     words = re.findall(r"[A-Za-z0-9]+", answer)
#     if len(words) >= 2:
#         pattern = r""
#         for w in words[:-1]:
#             pattern += re.escape(w) + r"(?:\s+|\W+)+"
#         pattern += re.escape(words[-1])

#         m = re.search(pattern, ctx, flags=re.IGNORECASE)
#         if m:
#             return ctx[m.start():m.end()]

#     # If we can't ground it, we prefer NO ANSWER (project goal: strong NoAns)
#     return NO_ANSWER_MARKER


# # ----------------------------
# # Batched generation
# # ----------------------------

# def _batch_generate(
#     tokenizer,
#     model,
#     device: torch.device,
#     prompts: List[str],
#     max_new_tokens: int,
#     max_length: int,
# ) -> List[str]:
#     inputs = tokenizer(
#         prompts,
#         return_tensors="pt",
#         padding=True,
#         truncation=True,
#         max_length=max_length,
#     )

#     input_ids = inputs["input_ids"].to(device)
#     attn = inputs["attention_mask"].to(device)

#     with torch.inference_mode():
#         out = model.generate(
#             input_ids=input_ids,
#             attention_mask=attn,
#             max_new_tokens=max_new_tokens,
#             do_sample=False,
#             pad_token_id=tokenizer.pad_token_id,
#             eos_token_id=tokenizer.eos_token_id,
#             use_cache=True,
#         )

#     gen = out[:, input_ids.shape[1]:]
#     return tokenizer.batch_decode(gen, skip_special_tokens=True)



# # ----------------------------
# # REQUIRED function: squad_qa
# # ----------------------------

# def squad_qa(data_filename: str) -> str:
#     """
#     Reads the sample CSV, generates a 'final answer' for each row,
#     and writes '<sample>-results.csv'. Returns the output filename.
#     """
#     tokenizer, model, device, max_input_tokens = _load_model_once()

#     df = pd.read_csv(data_filename)

#     # Output file path must match the template logic
#     out_filename = data_filename.replace(".csv", "-results.csv")

#     # Generation settings (tuned for speed + short answers)
#     batch_size = 4 if device.type == "cuda" else 1
#     max_new_tokens = 32

#     print(f"[squad_qa] rows={len(df)} device={device} batch_size={batch_size}")

#     results: List[str] = []

#     for start in range(0, len(df), batch_size):
#         chunk = df.iloc[start:start + batch_size]

#         prompts: List[str] = []
#         contexts: List[str] = []

#         for _, row in chunk.iterrows():
#             context = "" if pd.isna(row.get("context")) else str(row.get("context"))
#             question = "" if pd.isna(row.get("question")) else str(row.get("question"))

#             # Token-budget context so we keep question + instructions intact
#             context_trim = _truncate_context_to_fit(
#                 tokenizer=tokenizer,
#                 model=model,
#                 context=context,
#                 question=question,
#                 max_input_tokens=max_input_tokens,
#                 max_new_tokens=max_new_tokens,
#             )

#             messages = _build_messages(context_trim, question)

#             prompt = tokenizer.apply_chat_template(
#                 messages,
#                 tokenize=False,
#                 add_generation_prompt=True,
#             )

#             prompts.append(prompt)
#             contexts.append(context_trim)

#         # raw_answers = _batch_generate(tokenizer, model, prompts, max_new_tokens=max_new_tokens)
#         raw_answers = _batch_generate(tokenizer, model, device, prompts, max_new_tokens=max_new_tokens, max_length=max_input_tokens - max_new_tokens)


#         for raw, ctx in zip(raw_answers, contexts):
#             cleaned = _clean_model_text(raw)
#             grounded = _ground_to_context(cleaned, ctx)
#             results.append(grounded)

#         # lightweight progress for long runs
#         if (start + batch_size) % 50 == 0:
#             done = min(start + batch_size, len(df))
#             print(f"[squad_qa] Processed {done}/{len(df)}")


#     df["final answer"] = results
#     df.to_csv(out_filename, index=False)
#     print(f"final answers recorded into {out_filename}")
#     return out_filename

# if __name__ == '__main__':
#     start_time = time.time()

#     with open('config.json', 'r') as json_file:
#         config = json.load(json_file)

#     data = pd.read_csv(config['data'])
#     sample = data.sample(n=config['sample_for_solution'])  # for grading will be replaced with 'sample_for_grading'
#     sample_filename = config['data'].replace('.csv', '-sample.csv')
#     sample.to_csv(sample_filename, index=False)

#     out_filename = squad_qa(sample_filename)  # todo: the function you implement

#     eval_out = evaluate_results(out_filename, final_answer_column='final answer')
#     eval_out_list = [str((k, round(v, 3))) for (k, v) in eval_out.items()]
#     print('\n'.join(eval_out_list))

#     elapsed_time = time.time() - start_time
#     print(f"time: {elapsed_time: .2f} sec")

    ###################################################################################################################

import json
import re
import time
from typing import List, Tuple, Optional, Iterable

import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from utils.evaluate_results import NO_ANSWER_MARKER, evaluate_results

MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct"

# ============================================================
# Tuning knobs (RTX 4050 6GB friendly)
# ============================================================

# Batch sizes (auto-fallback on CUDA OOM)
BATCH_SIZE_CLASSIFY = 24   # classification is one forward pass (no generation)
BATCH_SIZE_ANSWER = 4      # answer generation is heavier

# Answer generation length (short = faster + better for SQuAD)
MAX_NEW_TOKENS_ANSWER = 24

# Context caps (major speed lever)
MAX_CTX_TOKENS_CLASSIFY = 256
MAX_CTX_TOKENS_ANSWER = 900

# Hard cap for total prompt length in tokens (major speed lever)
MAX_PROMPT_TOKENS_CAP = 1024

# Gate strictness: require YES score > NO score by this margin
# Higher => more conservative => better NoAns, maybe worse HasAns
ANSWERABLE_LOGIT_MARGIN = -0.5 # 4.4

# Progress printing
PRINT_EVERY = 50

WINDOW_STRIDE = 128
TOPK_ANSWER_WINDOWS = 2
TOPK_CLASSIFY_WINDOWS = 1


_STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "with",
    "is", "was", "are", "were", "be", "as", "by", "at", "from", "it", "this", "that"
}

# ============================================================
# Lazy globals
# ============================================================

_TOKENIZER: Optional[AutoTokenizer] = None
_MODEL: Optional[AutoModelForCausalLM] = None
_DEVICE: Optional[torch.device] = None
_MAX_INPUT_TOKENS: Optional[int] = None
# _YES_TOKEN_ID: Optional[int] = None
_YES_TOKEN_IDS: Optional[List[int]] = None
_NO_TOKEN_IDS: Optional[List[int]] = None


# ============================================================
# Model / Tokenizer
# ============================================================

def _get_device() -> torch.device:
    return torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    # return torch.device("cpu")


def _infer_max_input_tokens(model, tokenizer) -> int:
    max_pos = getattr(model.config, "max_position_embeddings", None)
    if isinstance(max_pos, int) and max_pos > 0:
        return min(max_pos, 8192)

    tmax = getattr(tokenizer, "model_max_length", None)
    if isinstance(tmax, int) and 0 < tmax < 10**6:
        return min(tmax, 8192)

    return 4096


VERIFY_MARGIN = 0.3  # start at 0.0; increase if too many false positives

def _verify_answer_supported(
    tokenizer: AutoTokenizer,
    model: AutoModelForCausalLM,
    device: torch.device,
    question: str,
    context: str,
    answer: str,
    max_length: int,
) -> bool:
    global _YES_TOKEN_IDS, _NO_TOKEN_IDS
    assert _YES_TOKEN_IDS is not None and _NO_TOKEN_IDS is not None

    if answer == NO_ANSWER_MARKER:
        return True

    msgs = [
        {"role": "system", "content": "You are a strict QA verifier. Reply ONLY YES or NO."},
        {"role": "user", "content":
            f"QUESTION:\n{question}\n\nCONTEXT:\n{context}\n\nPROPOSED ANSWER:\n{answer}\n\n"
            "Is the proposed answer fully supported by the context for this question? YES or NO: "
        },
    ]
    prompt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)

    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
    input_ids = inputs["input_ids"].to(device)
    attn = inputs["attention_mask"].to(device)

    yes_lp = _completion_logprob_sum(model, input_ids, attn, _YES_TOKEN_IDS, tokenizer.pad_token_id)
    no_lp  = _completion_logprob_sum(model, input_ids, attn, _NO_TOKEN_IDS, tokenizer.pad_token_id)

    return (yes_lp - no_lp).item() > VERIFY_MARGIN


def _keywords(question: str) -> List[str]:
    words = re.findall(r"[A-Za-z0-9]+", (question or "").lower())
    return [w for w in words if w not in _STOPWORDS and len(w) >= 3]


def _overlap_score(text: str, keys: List[str]) -> int:
    if not keys:
        return 0
    low = (text or "").lower()
    # count occurrences (cheap heuristic)
    return sum(low.count(k) for k in keys)


def _top_k_windows(
    tokenizer: AutoTokenizer,
    context: str,
    question: str,
    max_tokens: int,
    stride: int,
    top_k: int,
) -> List[str]:
    ctx = "" if context is None else str(context)
    if not ctx.strip():
        return [""]

    ids = tokenizer(ctx, add_special_tokens=False).input_ids
    if len(ids) <= max_tokens:
        return [ctx]

    keys = _keywords(question)

    step = max(1, max_tokens - stride)
    windows = []
    for start in range(0, len(ids), step):
        end = min(start + max_tokens, len(ids))
        chunk = tokenizer.decode(ids[start:end], skip_special_tokens=True)
        score = _overlap_score(chunk, keys)
        windows.append((score, start, chunk))
        if end == len(ids):
            break

    windows.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    best = [w[2] for w in windows[:top_k]]
    return best if best else [ctx]


def _completion_logprob_sum(
    model: AutoModelForCausalLM,
    input_ids: torch.Tensor,       # [B, L]
    attn: torch.Tensor,            # [B, L]
    completion_ids: List[int],     # length T
    pad_token_id: int,
) -> torch.Tensor:
    # Build completion tensor [B, T]
    B, L = input_ids.shape
    T = len(completion_ids)
    comp = torch.tensor(completion_ids, dtype=torch.long, device=input_ids.device).unsqueeze(0).repeat(B, 1)

    ext_ids = torch.cat([input_ids, comp], dim=1)                      # [B, L+T]
    ext_attn = torch.cat([attn, torch.ones((B, T), device=attn.device, dtype=attn.dtype)], dim=1)

    with torch.inference_mode():
        out = model(ext_ids, attention_mask=ext_attn)
        logits = out.logits  # [B, L+T, V]

    # Sum logprobs of completion tokens
    logp = torch.zeros((B,), device=input_ids.device)
    for t in range(T):
        # token at position (L+t) is predicted by logits at (L+t-1)
        step_logits = logits[:, L + t - 1, :]
        step_logp = torch.log_softmax(step_logits, dim=-1)
        tok = comp[:, t]
        logp += step_logp.gather(1, tok.unsqueeze(1)).squeeze(1)
    return logp


def _resolve_yes_no_token_ids(tokenizer: AutoTokenizer) -> Tuple[List[int], List[int]]:
    """
    Resolve single-token IDs for " YES" and " NO".
    For SentencePiece tokenizers, leading space often matters.
    We take the first token ID if encoding returns multiple tokens.
    """
    yes_ids = tokenizer.encode("YES", add_special_tokens=False)
    no_ids  = tokenizer.encode("NO", add_special_tokens=False)

    if not yes_ids:
        yes_ids = tokenizer.encode(" YES", add_special_tokens=False)
    if not no_ids:
        no_ids = tokenizer.encode(" NO", add_special_tokens=False)

    return yes_ids, no_ids


def _load_model_once() -> Tuple[AutoTokenizer, AutoModelForCausalLM, torch.device, int]:
    global _TOKENIZER, _MODEL, _DEVICE, _MAX_INPUT_TOKENS, _YES_TOKEN_IDS, _NO_TOKEN_IDS

    if _TOKENIZER is not None and _MODEL is not None and _DEVICE is not None and _MAX_INPUT_TOKENS is not None:
        return _TOKENIZER, _MODEL, _DEVICE, _MAX_INPUT_TOKENS

    device = _get_device()
    if device.type == "cuda":
        torch.backends.cuda.matmul.allow_tf32 = True

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"  # decoder-only batching

    dtype = torch.float16 if device.type == "cuda" else torch.float32

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        token=True,
        dtype=dtype,
        low_cpu_mem_usage=True,
    )
    model.to(device)
    model.eval()
    model.config.pad_token_id = tokenizer.pad_token_id

    # Silence noisy flags if present (not critical)
    if hasattr(model, "generation_config"):
        if hasattr(model.generation_config, "temperature"):
            model.generation_config.temperature = None
        if hasattr(model.generation_config, "top_p"):
            model.generation_config.top_p = None

    max_input_tokens = _infer_max_input_tokens(model, tokenizer)

    # _YES_TOKEN_ID, _NO_TOKEN_ID = _resolve_yes_no_token_ids(tokenizer)
    _YES_TOKEN_IDS, _NO_TOKEN_IDS = _resolve_yes_no_token_ids(tokenizer)


    _TOKENIZER, _MODEL, _DEVICE, _MAX_INPUT_TOKENS = tokenizer, model, device, max_input_tokens
    return tokenizer, model, device, max_input_tokens


# ============================================================
# Prompts
# ============================================================

def _system_prompt_answerable() -> str:
    return (
        "You are a QA assistant for SQuAD2.0.\n"
        "Decide if the QUESTION is answerable using ONLY the CONTEXT.\n"
        "Reply with exactly YES or NO.\n"
        "If you are not completely sure the answer is explicitly in the context, reply NO."
    )


def _system_prompt_answer() -> str:
    return (
        "You are a question answering assistant for SQuAD2.0.\n"
        "Use ONLY the given CONTEXT.\n"
        f"If the answer is not explicitly in the CONTEXT, reply exactly: {NO_ANSWER_MARKER}\n"
        "If answerable, reply with the shortest exact answer span copied verbatim from the CONTEXT.\n"
        "Reply with ONE line and nothing else."
    )


def _build_messages_answerable(question: str, context: str) -> List[dict]:
    user = (
        "QUESTION:\n"
        f"{question}\n\n"
        "CONTEXT:\n"
        f"{context}\n\n"
        "Answerable? (YES/NO):"
    )
    return [
        {"role": "system", "content": _system_prompt_answerable()},
        {"role": "user", "content": user},
    ]


def _build_messages_answer(question: str, context: str) -> List[dict]:
    user = (
        "QUESTION:\n"
        f"{question}\n\n"
        "CONTEXT:\n"
        f"{context}\n\n"
        "ANSWER:"
    )
    return [
        {"role": "system", "content": _system_prompt_answer()},
        {"role": "user", "content": user},
    ]


# ============================================================
# Context truncation (head+tail)
# ============================================================

def _truncate_context_tokens(tokenizer: AutoTokenizer, context: str, max_ctx_tokens: int) -> str:
    ctx = "" if context is None else str(context)
    if not ctx.strip():
        return ""

    ids = tokenizer(ctx, add_special_tokens=False).input_ids
    if len(ids) <= max_ctx_tokens:
        return ctx

    half = max_ctx_tokens // 2
    head = ids[:half]
    tail = ids[-(max_ctx_tokens - half):]
    return tokenizer.decode(head + tail, skip_special_tokens=True)


# ============================================================
# Cleaning, grounding, shrinking
# ============================================================

def _clean_first_line(text: str) -> str:
    if text is None:
        return ""
    text = text.strip()
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        return ""
    return lines[0].strip(" \t\r\n`\"'")


def _looks_like_no_answer(text: str) -> bool:
    if not text:
        return True
    t = text.strip().lower()
    if t == NO_ANSWER_MARKER.lower() or t.startswith(NO_ANSWER_MARKER.lower()):
        return True
    if any(p in t for p in [
        "not mentioned", "cannot be determined", "insufficient information",
        "not provided", "not stated", "unknown", "no information"
    ]):
        return True
    return False


def _ground_exact_or_fuzzy(answer: str, context: str) -> Optional[str]:
    ans = _clean_first_line(answer)
    if not ans:
        return None

    ctx = "" if context is None else str(context)
    if not ctx.strip():
        return None

    # exact
    idx = ctx.find(ans)
    if idx >= 0:
        return ans

    # case-insensitive
    low_ctx = ctx.lower()
    low_ans = ans.lower()
    idx = low_ctx.find(low_ans)
    if idx >= 0:
        return ctx[idx: idx + len(ans)]

    # regex word sequence
    words = re.findall(r"[A-Za-z0-9]+", ans)
    if len(words) >= 2:
        pattern = r""
        for w in words[:-1]:
            pattern += re.escape(w) + r"(?:\s+|\W+)+"
        pattern += re.escape(words[-1])
        m = re.search(pattern, ctx, flags=re.IGNORECASE)
        if m:
            return ctx[m.start():m.end()]

    return None


def _shrink_to_span(answer: str, context: str, max_ngram: int = 5) -> Optional[str]:
    ctx = "" if context is None else str(context)
    if not ctx.strip():
        return None

    words = re.findall(r"[A-Za-z0-9]+", _clean_first_line(answer))
    if not words:
        return None

    low_ctx = ctx.lower()
    max_n = min(max_ngram, len(words))

    for n in range(max_n, 0, -1):
        for i in range(0, len(words) - n + 1):
            cand_words = words[i:i + n]
            cand = " ".join(cand_words)

            if n == 1:
                w = cand_words[0].lower()
                if w in _STOPWORDS:
                    continue
                if len(w) < 3 and not w.isdigit():
                    continue

            idx = low_ctx.find(cand.lower())
            if idx >= 0:
                return ctx[idx: idx + len(cand)]

    return None


def _finalize_answer(answer_text: str, context: str, allow_shrink: bool) -> str:
    if _looks_like_no_answer(answer_text):
        return NO_ANSWER_MARKER

    grounded = _ground_exact_or_fuzzy(answer_text, context)
    if grounded is not None:
        return grounded

    if allow_shrink:
        shrunk = _shrink_to_span(answer_text, context)
        if shrunk is not None:
            return shrunk

    return NO_ANSWER_MARKER


# ============================================================
# Batch helpers + safe OOM fallback
# ============================================================

def _chunks_indices(n: int, batch_size: int) -> Iterable[Tuple[int, int]]:
    for start in range(0, n, batch_size):
        yield start, min(start + batch_size, n)


def _progress_print(phase: str, done: int, total: int, next_mark: int) -> int:
    """
    Print progress when 'done' passes next_mark; works with any batch size.
    """
    while done >= next_mark:
        print(f"[{phase}] {min(next_mark, total)}/{total}")
        next_mark += PRINT_EVERY
    if done == total:
        print(f"[{phase}] {total}/{total}")
    return next_mark


# ============================================================
# Priority A: Answerability via logits (fast, no generation)
# ============================================================

# def _answerable_gate_scores(
#     tokenizer: AutoTokenizer,
#     model: AutoModelForCausalLM,
#     device: torch.device,
#     prompts: List[str],
#     max_length: int,
#     batch_size: int,
# ) -> List[bool]:
#     global _YES_TOKEN_IDS, _NO_TOKEN_IDS
#     assert _YES_TOKEN_IDS is not None and _NO_TOKEN_IDS is not None

#     results: List[bool] = []
#     bs = batch_size
#     next_mark = PRINT_EVERY

#     while True:
#         try:
#             for start, end in _chunks_indices(len(prompts), bs):
#                 batch_prompts = prompts[start:end]
#                 inputs = tokenizer(
#                     batch_prompts,
#                     return_tensors="pt",
#                     padding=True,
#                     truncation=True,
#                     max_length=max_length,
#                 )
#                 input_ids = inputs["input_ids"].to(device)
#                 attn = inputs["attention_mask"].to(device)

#                 with torch.inference_mode():
#                     gen_out = model.generate(
#                         input_ids=input_ids,
#                         attention_mask=attn,
#                         max_new_tokens=1,
#                         do_sample=False,
#                         pad_token_id=tokenizer.pad_token_id,
#                         eos_token_id=tokenizer.eos_token_id,
#                         use_cache=True,
#                         return_dict_in_generate=True,
#                         output_scores=True,
#                     )

#                 # scores[0] is logits for the first generated token: [B, V]
#                 scores0 = gen_out.scores[0]
#                 yes = scores0[:, _YES_TOKEN_IDS]
#                 no = scores0[:, _NO_TOKEN_IDS]
#                 is_yes = (yes - no) > ANSWERABLE_LOGIT_MARGIN
#                 results.extend(is_yes.detach().cpu().tolist())

#                 next_mark = _progress_print("classify", end, len(prompts), next_mark)

#             return results
#         except RuntimeError as e:
#             if device.type == "cuda" and "out of memory" in str(e).lower():
#                 torch.cuda.empty_cache()
#                 if bs <= 1:
#                     raise
#                 new_bs = max(1, bs // 2)
#                 print(f"[classify] CUDA OOM at batch_size={bs}. Retrying with batch_size={new_bs}...")
#                 bs = new_bs
#                 results = []
#                 next_mark = PRINT_EVERY
#                 continue
#             raise

def _answerable_gate_scores(
    tokenizer: AutoTokenizer,
    model: AutoModelForCausalLM,
    device: torch.device,
    prompts: List[str],
    max_length: int,
    batch_size: int,
) -> List[bool]:
    global _YES_TOKEN_IDS, _NO_TOKEN_IDS
    assert _YES_TOKEN_IDS is not None and _NO_TOKEN_IDS is not None

    results: List[bool] = []
    bs = batch_size
    next_mark = PRINT_EVERY

    while True:
        try:
            for start, end in _chunks_indices(len(prompts), bs):
                batch_prompts = prompts[start:end]
                inputs = tokenizer(
                    batch_prompts,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=max_length,
                )
                input_ids = inputs["input_ids"].to(device)
                attn = inputs["attention_mask"].to(device)

                yes_lp = _completion_logprob_sum(model, input_ids, attn, _YES_TOKEN_IDS, tokenizer.pad_token_id)
                no_lp  = _completion_logprob_sum(model, input_ids, attn, _NO_TOKEN_IDS, tokenizer.pad_token_id)

                diff = yes_lp - no_lp
                is_yes = diff > ANSWERABLE_LOGIT_MARGIN   # margin now in logprob units!
                results.extend(is_yes.detach().cpu().tolist())

                next_mark = _progress_print("classify", end, len(prompts), next_mark)

            return results

        except RuntimeError as e:
            if device.type == "cuda" and "out of memory" in str(e).lower():
                torch.cuda.empty_cache()
                if bs <= 1:
                    raise
                bs = max(1, bs // 2)
                print(f"[classify] CUDA OOM. Retrying with batch_size={bs}...")
                results = []
                next_mark = PRINT_EVERY
                continue
            raise


# ============================================================
# Answer generation (only for answerable indices)
# ============================================================

def _generate_answers(
    tokenizer: AutoTokenizer,
    model: AutoModelForCausalLM,
    device: torch.device,
    prompts: List[str],
    max_length: int,
    batch_size: int,
) -> List[str]:
    outputs: List[str] = []
    bs = batch_size
    next_mark = PRINT_EVERY

    while True:
        try:
            for start, end in _chunks_indices(len(prompts), bs):
                batch_prompts = prompts[start:end]
                inputs = tokenizer(
                    batch_prompts,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=max_length,
                )
                input_ids = inputs["input_ids"].to(device)
                attn = inputs["attention_mask"].to(device)

                with torch.inference_mode():
                    out = model.generate(
                        input_ids=input_ids,
                        attention_mask=attn,
                        max_new_tokens=MAX_NEW_TOKENS_ANSWER,
                        do_sample=False,
                        pad_token_id=tokenizer.pad_token_id,
                        eos_token_id=tokenizer.eos_token_id,
                        use_cache=True,
                    )

                gen = out[:, input_ids.shape[1]:]
                outputs.extend(tokenizer.batch_decode(gen, skip_special_tokens=True))

                next_mark = _progress_print("answer", end, len(prompts), next_mark)

            return outputs
        except RuntimeError as e:
            if device.type == "cuda" and "out of memory" in str(e).lower():
                torch.cuda.empty_cache()
                if bs <= 1:
                    raise
                new_bs = max(1, bs // 2)
                print(f"[answer] CUDA OOM at batch_size={bs}. Retrying with batch_size={new_bs}...")
                bs = new_bs
                outputs = []
                next_mark = PRINT_EVERY
                continue
            raise


# ============================================================
# REQUIRED function: squad_qa
# ============================================================

def squad_qa(data_filename: str) -> str:
    tokenizer, model, device, max_input_tokens = _load_model_once()

    df = pd.read_csv(data_filename)
    out_filename = data_filename.replace(".csv", "-results.csv")

    prompt_cap = min(max_input_tokens, MAX_PROMPT_TOKENS_CAP)

    print(
        f"[squad_qa] rows={len(df)} device={device} "
        f"bs_cls={BATCH_SIZE_CLASSIFY} bs_ans={BATCH_SIZE_ANSWER} "
        f"prompt_cap={prompt_cap}"
    )

    questions = df["question"].fillna("").astype(str).tolist()
    contexts_full = df["context"].fillna("").astype(str).tolist()

    # -------------------------
    # A) Answerability gate (logits)
    # -------------------------
    contexts_cls_list = [
        _top_k_windows(tokenizer, c, q, MAX_CTX_TOKENS_CLASSIFY, WINDOW_STRIDE, TOPK_CLASSIFY_WINDOWS)
        for q, c in zip(questions, contexts_full)
    ]

    cls_prompts = [
        tokenizer.apply_chat_template(
            _build_messages_answerable(q, c_list[0]),  # best classify window
            tokenize=False,
            add_generation_prompt=True,
        )
        for q, c_list in zip(questions, contexts_cls_list)
    ]


    print("[classify] starting...")
    is_answerable = _answerable_gate_scores(
        tokenizer=tokenizer,
        model=model,
        device=device,
        prompts=cls_prompts,
        max_length=prompt_cap,  # full cap; classification is just forward
        batch_size=BATCH_SIZE_CLASSIFY if device.type == "cuda" else 1,
    )

    answerable_indices = [i for i, ok in enumerate(is_answerable) if ok]
    print(
        f"[squad_qa] answerable_gate: YES={len(answerable_indices)} / {len(df)} "
        f"({len(answerable_indices)/max(1,len(df))*100:.1f}%)"
    )

    # conservative default
    final_answers = [NO_ANSWER_MARKER] * len(df)

    if not answerable_indices:
        df["final answer"] = final_answers
        df.to_csv(out_filename, index=False)
        print(f"final answers recorded into {out_filename}")
        return out_filename

    # -------------------------
    # Generate answers only for YES
    # -------------------------
    # contexts_ans = [_truncate_context_tokens(tokenizer, c, MAX_CTX_TOKENS_ANSWER) for c in contexts_full]
    # contexts_ans_list = [
    #     _top_k_windows(tokenizer, c, q, MAX_CTX_TOKENS_ANSWER, WINDOW_STRIDE, TOPK_ANSWER_WINDOWS)
    #     for q, c in zip(questions, contexts_full)
    # ]

    # ans_prompts: List[str] = []
    # ans_contexts: List[str] = []
    # ans_positions: List[int] = []

    # for i in answerable_indices:
    #     q = questions[i]
    #     c = contexts_ans_list[i][0]
    #     ans_prompts.append(
    #         tokenizer.apply_chat_template(
    #             _build_messages_answer(q, c),
    #             tokenize=False,
    #             add_generation_prompt=True,
    #         )
    #     )
    #     ans_contexts.append(c)
    #     ans_positions.append(i)

    # print("[answer] starting...")
    # raw_answers = _generate_answers(
    #     tokenizer=tokenizer,
    #     model=model,
    #     device=device,
    #     prompts=ans_prompts,
    #     max_length=prompt_cap - MAX_NEW_TOKENS_ANSWER,
    #     batch_size=BATCH_SIZE_ANSWER if device.type == "cuda" else 1,
    # )

    # -------------------------
    # Generate answers only for YES (with window fallback)
    # -------------------------
    contexts_ans_list = [
        _top_k_windows(tokenizer, c, q, MAX_CTX_TOKENS_ANSWER, WINDOW_STRIDE, TOPK_ANSWER_WINDOWS)
        for q, c in zip(questions, contexts_full)
    ]

    # conservative default already set: final_answers = [NO_ANSWER_MARKER] * len(df)
    pending = list(answerable_indices)

    # Try windows in order: window 0, then window 1 (up to TOPK_ANSWER_WINDOWS)
    for w in range(TOPK_ANSWER_WINDOWS):
        if not pending:
            break

        ans_prompts: List[str] = []
        ans_contexts: List[str] = []
        ans_positions: List[int] = []

        for i in pending:
            q = questions[i]
            wins = contexts_ans_list[i]
            # Safety: if fewer windows exist than expected, reuse the last available
            ctx = wins[w] if w < len(wins) else wins[-1]

            ans_prompts.append(
                tokenizer.apply_chat_template(
                    _build_messages_answer(q, ctx),
                    tokenize=False,
                    add_generation_prompt=True,
                )
            )
            ans_contexts.append(ctx)
            ans_positions.append(i)

        print(f"[answer] starting... (window {w+1}/{TOPK_ANSWER_WINDOWS}, n={len(ans_prompts)})")
        raw_answers = _generate_answers(
            tokenizer=tokenizer,
            model=model,
            device=device,
            prompts=ans_prompts,
            max_length=prompt_cap - MAX_NEW_TOKENS_ANSWER,
            batch_size=BATCH_SIZE_ANSWER if device.type == "cuda" else 1,
        )

        next_pending: List[int] = []

        for raw, ctx, pos in zip(raw_answers, ans_contexts, ans_positions):
            cand = _finalize_answer(raw, ctx, allow_shrink=True)

            if cand != NO_ANSWER_MARKER:
                ok = _verify_answer_supported(
                    tokenizer=tokenizer,
                    model=model,
                    device=device,
                    question=questions[pos],
                    context=ctx,
                    answer=cand,
                    max_length=prompt_cap,
                )
                if ok:
                    final_answers[pos] = cand
                else:
                    next_pending.append(pos)
            else:
                next_pending.append(pos)

        pending = next_pending


    # -------------------------
    # C) Grounding + shrink-to-span
    # -------------------------
    # for raw, ctx, pos in zip(raw_answers, ans_contexts, ans_positions):
    #     final_answers[pos] = _finalize_answer(raw, ctx, allow_shrink=True)
    # for raw, ctx, pos in zip(raw_answers, ans_contexts, ans_positions):
    #     cand = _finalize_answer(raw, ctx, allow_shrink=True)

    #     if cand != NO_ANSWER_MARKER:
    #         ok = _verify_answer_supported(
    #             tokenizer=tokenizer,
    #             model=model,
    #             device=device,
    #             question=questions[pos],
    #             context=ctx,
    #             answer=cand,
    #             max_length=prompt_cap,
    #         )
    #         final_answers[pos] = cand if ok else NO_ANSWER_MARKER
    #     else:
    #         final_answers[pos] = NO_ANSWER_MARKER


    df["final answer"] = final_answers
    df.to_csv(out_filename, index=False)
    print(f"final answers recorded into {out_filename}")
    return out_filename


# ============================================================
# Entrypoint
# ============================================================

if __name__ == "__main__":
    start_time = time.time()

    with open("config.json", "r", encoding="utf-8") as json_file:
        config = json.load(json_file)

    data = pd.read_csv(config["data"])
    sample = data.sample(n=int(config["sample_for_solution"]), random_state=0)  # grader may change to sample_for_grading
    sample_filename = config["data"].replace(".csv", "-sample.csv")
    sample.to_csv(sample_filename, index=False)

    out_filename = squad_qa(sample_filename)

    eval_out = evaluate_results(out_filename, final_answer_column="final answer")
    eval_out_list = [str((k, round(v, 3))) for (k, v) in eval_out.items()]
    print("\n".join(eval_out_list))

    elapsed_time = time.time() - start_time
    print(f"time: {elapsed_time: .2f} sec")
