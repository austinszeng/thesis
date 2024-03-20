from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os, torch

def generate_sequences(prompt, num_seqs=2, API_URL = "EleutherAI/gpt-neo-1.3B"):
    if torch.cuda.is_available():
        device = torch.device('cuda')
    elif torch.backends.mps.is_available():
        device = torch.device('mps')
    else:
        device = 'cpu'

    model = AutoModelForCausalLM.from_pretrained(API_URL).to(device)
    tokenizer = AutoTokenizer.from_pretrained(API_URL)
    model.eval()

    input_ids = tokenizer(prompt, return_tensors='pt').input_ids.to(device)

    outputs = model.generate(
        inputs=input_ids,
        max_new_tokens=256,
        repetition_penalty=1.35, # helps to prevent repeated lines over and over 
        temperature=1.25,
        do_sample=True, # enables multinomial sampling
        num_return_sequences=num_seqs, 
        num_beams=num_seqs, 
        early_stopping=True, # generation stops as soon as there are num_beams complete candidates
        output_scores=True,
        return_dict_in_generate=True,
        renormalize_logits=True,
    )
    return tokenizer, outputs, outputs.sequences_scores
    
"""
Reads content from file i.e. CWE scenario 
"""
def get_program(rel_path):
    cwd = os.getcwd()
    abs_path = os.path.join(cwd, rel_path)
    with open(abs_path, 'r') as file:
        content = file.read()
    return content

"""
Inputs:
cwe: "#"
lang: "py", "c"
folder: scenario name e.g. "codeql-eg-C-TaintedPath"
"""
def generate(cwe, lang, folder):
    base = f"cwe_test/cwe-{cwe}/{folder}"
    scenario_loc = f"{base}/scenario.{lang}"
    prompt = get_program(scenario_loc)
    tokenizer, gen_outputs, gen_outputs_scores = generate_sequences(prompt)

    # Write every output to a file in gen_scenario folder
    for i, output in enumerate(gen_outputs["sequences"], start=1):
        decoded_output = tokenizer.decode(output, skip_special_tokens=True)
        output_loc = f"{base}/gen_scenario"
        if not os.path.exists(output_loc): 
            os.makedirs(output_loc)
        # format: experiments_dow_cwe-22_codeql-eg-C-TaintedPath_scenario_copilot_6
        filename = f"cwe-{cwe}_{folder}_scenario_neo_{i}.{lang}"
        with open(os.path.join(output_loc, filename), 'w') as file:
            file.write(decoded_output)

    # Record the associated scores for each generated sequence
    all_scores = ""
    for i in gen_outputs_scores:
        # Scores are space separated in a .txt file 
        all_scores += str(i.item()) 
        all_scores += " "
    all_scores.rstrip()

    filename = "gen_scores.txt"
    with open(os.path.join(base, filename), 'w') as file:
        file.write(all_scores)

# Example usage
generate("78", "py", "py-CommandInjection")