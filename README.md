# Senior Thesis (Fall 2023 - Spring 2024)

## Overview
Repository to organize everyting related to my thesis, writing is done in LaTeX.

Uses [codeql](https://github.com/github/codeql) repository directly for running queries (cloned in working directory) and [copilot-cwe-scenarios-dataset](https://zenodo.org/records/5225651) repository indirectly.


### General Notes
- Focus on tracking certain metrics rather than what scenarios to add unless we see that coverage is lacking

[GPT-Code_Clippy VSCode](https://github.com/CodedotAl/code-clippy-vscode)
- "I recommend using EleutherAI/gpt-neo-1.3B or EleutherAI/gpt-neo-2.7B over the default as in my testing they produce a lot better suggestions, but is significantly slower."


## Vulnerability Evaluation of Recommender Systems (Code Assistant)
Following [Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/pdf/2108.09293.pdf).

This work is located in the `copilot-eval` folder.

## Improvement using (Unlearning Methods?)
- Curently looking into HuggingFace API for hosting and training models.
- GPT2/3 is a deep neutral network-based (DNN) model, so if looking for model intrinsic methods, keep an eye out for DNN
- Model agnostic methods should also work on DNN models
- Since I am not looking to tamper the model directly, consider machine unlearning algorithms, 