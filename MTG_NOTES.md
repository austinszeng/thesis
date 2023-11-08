# Meeting Notes
This is just for my own convenience and organizational purposes.

## Overarching/Current Goals

### Implement open source code recommender model into testing framework, completing the reproduction of the "Asleep at the Keyboard" paper's framework

#### Primary
- [ ] Understand how Clippy VSCode uses inference API (what tokenizer? what parameters?)
    - [ ] If needed: tutorial video on how to use `transformers` library for code generation
- [x] Utilize Inference API to generate text using one of Clippy's models 
- [ ] Utilize Inference API to generate top (25) suggestions given an input
- [ ] CodeQL analysis on outputted programs
- [ ] Initial rough comparison of vulnerabilities in comparison to original paper's analysis of same scenario (`Purpose`: Copilot vs GPT-Code_clippy)
- [ ] Replace `gen_scenario` folder, `Copilot` file, and `.csv` results with own outputs from HuggingFace API
- [ ] Tweak prompts to fit our model (as needed)
    - [ ] Look at usage models provided by model/ experiment with restating prompts to find good baseline performance
#### Secondary
- [ ] Output Rank/confidence in addition to suggestion
- [ ] Implement retraining/ model modification loop (?)
#### Non-priority
- [ ] Present CSV statistics in a clear way (how to go about this? Python script that gets run in the bash script that cleans up the CodeQL generated CSV?)
- [ ] Create a diagram of how Laptop interacts with server for Inference API

### Build general understanding of different types of models, what does this mean for the training/unlearning methods we have available 
- [ ] DNN vs GNN vs all other models

### Research: unlearning methods 
- [ ] Model intrinsic DNN unlearning reading
- [ ] Model agnostic unlearning reading
1. What changes to evaluate?
- [ ] Learn about different model training techniques (reading)
- [ ] How do we actually apply these strategies to the model?
2. What tests will help us evaluate the effect of changes? 
- [ ] Decide on the "useful" columns of the CSV output (What changes do we hope to appear?)



## Meetings
#### 11/3
- diagram of laptop interacting with server for api
- API figures out how to swap model
- tweak prompts to fit our model (as needed)
    - look at usage models provided by model?
    - backup: experiment with restating prompts to find good baseline performance
- output rank/confidence in addition to suggestion
- implementing retraining/ model modification loop

- look into pipeline documentation and tutorial video 
- look around pipeline parameters
- how to use transformers to study code generation...what defaults do we use?
- tutorials specific to code generation

- understand how clippy vscode uses inference api (what tokenizer is used? what parameters?) translate to python?
    - rank/ confidence is secondary...


#### 10/27
- Outline example:
    - intro (code recommenders output insecure code)
    - background
        - related work
        - high level problem motivation (how do we know?)
        - general terms and concepts
            - "methods exist that are more efficient than retraining the whole model from scratch"
    - methods
        - based on background, what is our approach/ why did we choose it?
    - system (code, pipeline)
        - pseudocode/ description of major pieces and what each does (maybe put code in an appendix? github?)
    - experimental design
        - what experiments did we run? what CWEs we chose? which metrics, etc.
    - results (analysis, discussion)
    - conclusion
- Check-in: annotated bib, outline, or code (testing framework with HF api and documentation of how to use, what comes out) for check-in 
- need to understand landscape of methods 

- Focus 10/28-11/3:
    - huggingface api working, plugged into pipeline
        - does clippy have "ranking" of suggestions/ capability of outputting multiple suggestions? (if no, talk about workarounds)
    - DNN vs GNN vs all other models? (building high level understanding of models) and what does this mean for the methods we have available
    - unlearning reading (ongoing...)


#### Completed Tasks (Dump)
Keeping track of some of them for later reference on the process maybe.

- [x] `Logistics`: look into hosting and training models on HuggingFace
- [x] Create a set of CWE scenarios ready to be tested (code scenarios from paper and associated `.ql` files from `codeql` repo)
- [x] Write a bash script to run CodeQL commands e.g. create database, use associated query to do analysis (`Purpose`: automate testing process)
- [x] Implementing API allows ability to swap out models with ease
