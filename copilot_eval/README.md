# Notes

## References
HF Inference API
- [Pipelines](https://huggingface.co/docs/transformers/main_classes/pipelines)
- [StoppingCriteria](https://huggingface.co/docs/transformers/v4.35.2/en/internal/generation_utils#transformers.StoppingCriteria)
- [Text2TextGenerationPipeline](https://huggingface.co/docs/transformers/v4.35.2/en/main_classes/pipelines#transformers.Text2TextGenerationPipeline)

## Bugs
- [ ] Figure out how to properly work with pipeline generator
    - Use it to generate each token, similar to how [StarCoder Playground](https://huggingface.co/spaces/bigcode/bigcode-playground/blob/main/app.py) implements generation using the Client class
    - "generated_text" otuputs the whole chunk of code, so the `stop_token` isn't even used (look into [documentation](https://huggingface.co/docs/transformers/main_classes/pipelines))


## Extended Requirements
### PyTorch installation (depends on OS)
Refer to: [PyTorch](https://pytorch.org/get-started/locally)
- `requirements.txt` is compatible for MacOS

## Input to focus on
I think it makes sense to focus on the "Diversity of weakness" scenarios since this category of scenarios is the simplst in terms of writing prompts for the goal of possibly introducing a CWE ("Diversity of prompt" plays around with minute changes and "Diversity of domain" looks at lesser used languages).

### Potential CWE's to focus on (pick 1-2 from "Diversity of weakness" scenarios):
1. `CWE-78`
    - 78-0: All programs vulnerable
    - 78-1: Confident in vulnerable answers (ExecTainted)
    - 78-2: (Python) top suggestion non-vulnerable (CommandInjection)
2. `CWE-22`
    - very vulnerable, all but one is vulnerable for C.
3. `CWE-306`
    - copilot did well (But unable to test w/ queries b/c these are custom scenarios)
4. `CWE-732`
    - non-vulnerable top suggestions + overall did well

`Note`: CWE-306 and CWE-732 can be useful to check if future improvements decrease performance in previously good areas


## Decide on what and how to grade
Out of (many) generated code-generated programs from our scenario, we will use CodeQL to evaluate whether any vulnerability exists. 

We will take a percentage of programs that have a vulnerability.

If possible: similar to the paper, we will create box plots of non-vulnerable vs. vulnerable programs against the code assistant's (probability) score for each CWE scenario.

## Running Code Generation script:
TO-DO: Explain what it does...

- Need to be logged in to HuggingFace CLI

## Basic CodeQL Workflow:
This is automated with the `main.sh` script's `run_codeql` function. Check comments for parameters.

1. Create Database:

Database should be created for each CWE scenario group of the Copilot generated programs.

```
codeql database create <database-name> --language=<lang> --source-root=<relative-path-to-code>
```
e.g. 
```
codeql database create test_db --language=python --source-root=cwe_test/py-CommandInjection/gen_scenario
```

2. Write Queries

Find existing queries in [codeql repository](https://github.com/github/codeql) in "codeql/\<lang\>/ql/src/Security".

3. Run Analysis
```
codeql database analyze <database> --format=<format> --output=<output> <query-specifiers>...
```

If CodeQL repository is checked out, queries can be executed by specifying the path to the query:

e.g.
```
codeql database analyze <database> ~/Desktop/thesis/codeql/<lang>/ql/src/Security/CWE-<number>/<query>.ql --format=csv --output=<rel_path/output_filename>.csv 
```

example `--output=cwe_test/cwe-78/CommandInjection/test_ql_results.csv`

## References:
- [GPT-Code_clippy](https://github.com/CodedotAl/gpt-code-clippy)
- [CWE Top 25](https://cwe.mitre.org/data/definitions/1425.html)
- [CodeQL Set-up](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis)
- [CodeQL Analysis](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries)
- [What does CodeQL output in CSV?](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/csv-output#about-csv-output) 