from transformers import AutoTokenizer, pipeline, StoppingCriteria, StoppingCriteriaList
from cleaner import get_program
import torch

class StopCrit (StoppingCriteria):
    def __init__(self, stops = [], encounters=1):
        super().__init__()
        self.stops = stops
        self.ENCOUNTERS = encounters

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor):
      stop_count = 0
      for stop in self.stops:
        stop_count = (stop == input_ids[0]).sum().item()
      if stop_count >= self.ENCOUNTERS:
          return True
      return False

# API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
""" Models to test:
EleutherAI/gpt-neo-2.7B
flax-community/gpt-neo-125M-code-clippy
"""
API_URL = "flax-community/gpt-neo-125M-code-clippy"
tokenizer = AutoTokenizer.from_pretrained(API_URL)

# Returns a Text2TextGenerationPipeline 
# StoppingCriteria class to apply stopping criteria during generation
generator = pipeline("text-generation", model=API_URL, tokenizer=API_URL)

# stop_token="<|endoftext|>"
def generate(prompt, temperature=0.2, max_new_tokens=256, top_p=0.9, repetition_penalty=1.2):
    temperature = float(temperature)
    top_p = float(top_p)

    # Declare stop list
    stop_words_ids = [tokenizer(stop_word, return_tensors='pt')['input_ids'].squeeze() for stop_word in ["###"]]
    stopping_criteria = StoppingCriteriaList([StopCrit(stops=stop_words_ids, encounters=1)])

    generate_kwargs = dict(
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        stopping_criteria=stopping_criteria,
        num_return_sequences=2,
    )

    outputs = generator(prompt, **generate_kwargs)

    for response in outputs:
        # This just prints a whole block of generated text...so need
        # to utilize StoppingCriteria for the generator probably instead
        # of doing this...
        print(response)
        out = ""
        generated_text = response["generated_text"].strip()
        out += generated_text
        yield out
    return out

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

