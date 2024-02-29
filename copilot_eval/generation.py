from transformers import AutoTokenizer, pipeline
from cleaner import get_program

""" GPT-Neo models:
EleutherAI/gpt-neo-125m
EleutherAI/gpt-neo-1.3B
EleutherAI/gpt-neo-2.7B
"""
API_URL = "EleutherAI/gpt-neo-1.3B"
tokenizer = AutoTokenizer.from_pretrained(API_URL)

# Returns a Text2TextGenerationPipeline 
generator = pipeline("text-generation", model=API_URL, tokenizer=API_URL)

def generate(prompt, temperature=0.2, max_new_tokens=256, top_p=0.9, repetition_penalty=1.2):
    temperature = float(temperature)
    top_p = float(top_p)
    generate_kwargs = dict(
        max_new_tokens=max_new_tokens,
        # temperature=temperature,
        # top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True, # enables multinomial sampling
        num_return_sequences=3,
        early_stopping=True,
        num_beams=5,
    )

    outputs = generator(prompt, **generate_kwargs)
    for response in outputs:
        out = ""
        generated_text = response["generated_text"].strip()
        out += generated_text
        yield out
    return out

"""
TO-DOs:
- wrap above in a function
- turn example usage into arguments...
- after finetuning the parameters for generation,
- create a separately defined folder where outputted sequences will have programs created (based on whether python or c)
    so that codeql script can reference these files to be analyzed..
    - essentially, put all the previously printed code into their own files
"""

# Example usage
cwe = "cwe-78"
lang = "py"
folder = lang + "-" + "CommandInjection"
location = "cwe_test/" + cwe + "/" + folder + "/scenario.py"
prompt = get_program(location)

output_generator = generate(prompt)

# Replace this with a function that creates a new .py or .c file in 
# location2 = "cwe_test/" + cwe + "/" + folder 
# for each output...

for output in output_generator:
    print("SEQ: ")
    print(output, "\n\n")
