import re, os

# Dummy: returns the input code unchanged
def regex(input_code):
    # Captures entire input
    pattern = r'(.*)'
    # \1 matches the contents of group 1 (the whole input)
    out = re.sub(pattern, r'\1', input_code)
    # (?) Future implementation: output the code as a new "fixed" file if changes were made 
    return out

def get_program(rel_path):
    cwd = os.getcwd()
    abs_path = os.path.join(cwd, rel_path)
    with open(abs_path, 'r') as file:
        content = file.read()
    return content
