# Senior Thesis (Fall 2023 - Spring 2024)

## Overview
Repository to organize everyting related to my thesis, writing is done in LaTeX.

Uses [codeql](https://github.com/github/codeql) repository directly for running queries (cloned in working directory) and [copilot-cwe-scenarios-dataset](https://zenodo.org/records/5225651) repository indirectly.

## Meeting Notes/ TO-DOs

### Building Pipeline
- [ ] `Logistics`: look into hosting and training models on HuggingFace
- [x] Create a set of CWE scenarios ready to be tested (code scenarios from paper and associated `.ql` files from `codeql` repo)
- [ ] Use HuggingFace API to input scenarios into GPT-Code_clippy model and get a set of (25) code-generated programs out (Swap Copilot for Open Source Code assistant in pipeline)
    - [ ] Use CodeQL to do analysis on these programs
    - [ ] Initial rough comparison of vulnerabilities in comparison to original paper's analysis of same scenario (`Purpose`: Copilot vs GPT-Code_clippy)
- [x] Write a bash script to run CodeQL commands e.g. create database, use associated query to do analysis (`Purpose`: automate testing process)
- [ ] Present CSV statistics in a clear way (how to go about this? Python script that gets run in the bash script that cleans up the CodeQL generated CSV?)
- [ ] Replace `gen_scenario` folder, `Copilot` file, and `.csv` results with own outputs from HuggingFace API

### Experimental design
1. What changes to evaluate?
- [ ] Learn about different model training techniques (reading)
    - [ ] First, revisit unlearning article
- [ ] How do we actually apply these strategies to the model?
2. What tests will help us evaluate the effect of changes? 
- [ ] Decide on the "useful" columns of the CSV output (What changes do we hope to appear?)

### Misc.
- [x] Make a rough table of contents in LaTeX
- [ ] Check if GPT-Code_clippy can provide a probability/ ranking score for its (25) generated outputs

### General Notes
- Focus on tracking certain metrics rather than what scenarios to add unless we see that coverage is lacking

[GPT-Code_Clippy VSCode](https://github.com/CodedotAl/code-clippy-vscode)
- "I recommend using EleutherAI/gpt-neo-1.3B or EleutherAI/gpt-neo-2.7B over the default as in my testing they produce a lot better suggestions, but is significantly slower."




## Vulnerability Evaluation of Recommender Systems (Code Assistant)
Following [Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/pdf/2108.09293.pdf).

This work is located in the `copilot-eval` folder.

## Improvement using (Unlearning Methods?)
Curently looking into HuggingFace API for hosting and training models.