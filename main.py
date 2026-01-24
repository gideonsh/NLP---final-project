import json
import pandas as pd
import time
import torch
torch.set_default_device('cpu')

from transformers import AutoModelForCausalLM, AutoTokenizer
from utils.evaluate_results import NO_ANSWER_MARKER, evaluate_results


model_name = 'meta-llama/Llama-3.2-3B-Instruct'
tokenizer = AutoTokenizer.from_pretrained(model_name, token=True)
model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.float16, token=True)
model.config.pad_token_id = tokenizer.eos_token_id
tokenizer.pad_token_id = tokenizer.eos_token_id


def squad_qa(data_filename):

    # todo: implement this function, design your solution and document properly

    # todo: you will need to sign up for huggingface and visit https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct to get access
    # todo: squad2.0 dataset - https://huggingface.co/datasets/rajpurkar/squad_v2


    out_filename = data_filename.replace('.csv', '-results.csv')
    print(f'final answers recorded into {out_filename}')
    return out_filename


if __name__ == '__main__':
    start_time = time.time()

    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

    data = pd.read_csv(config['data'])
    sample = data.sample(n=config['sample_for_solution'])  # for grading will be replaced with 'sample_for_grading'
    sample_filename = config['data'].replace('.csv', '-sample.csv')
    sample.to_csv(sample_filename, index=False)

    out_filename = squad_qa(sample_filename)  # todo: the function you implement

    eval_out = evaluate_results(out_filename, final_answer_column='final answer')
    eval_out_list = [str((k, round(v, 3))) for (k, v) in eval_out.items()]
    print('\n'.join(eval_out_list))

    elapsed_time = time.time() - start_time
    print(f"time: {elapsed_time: .2f} sec")
