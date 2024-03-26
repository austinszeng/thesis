# Testing Framework

Structure and workflow is based on the "Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions" paper (henceforth PAT+) for code vulnerability analysis found in this [repository](https://zenodo.org/records/5225651).

## Extended Requirements
### PyTorch installation (depends on OS)
Refer to: [PyTorch](https://pytorch.org/get-started/locally)
- `requirements.txt` is compatible for Mac
### Install [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli)

## Get Started
To replicate results, run `generation.py` and `run_main.sh`. 

## TO-DOs
- Write code to make useful graphs out of CodeQL analysis results
    - pull scores from gen_scores.txt
    - associate top program and whether it was vulnerable

## Code Generation Script
Main function is `generate`, which generates sequences through `GPT-Neo 1.3B` inference using the HuggingFace `transformers`, then creates a folder where each of these sequences have their own program files to be evaluated for vulnerabilities in the next step.

## Basic CodeQL Workflow:
To evaluate whether vulnerabilities exist for each CWE scenario, we run CodeQL queries to identify for that given CWE. This will allow us to take a percentage of programs that have a vulnerability among other analysis metrics, like percentage of top probability programs that are vulnerable.

This is automated with the `main.sh` script's `run_codeql` function. 

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

Most queries were found in the [codeql repository](https://github.com/github/codeql). Associated queries for each scenario are within the same folder.

3. Run Analysis
```
codeql database analyze <database> --format=<format> --output=<output> <query-specifiers>...
```
e.g.
```
codeql database analyze <database> ~/Desktop/thesis/codeql/<lang>/ql/src/Security/CWE-<number>/<query>.ql --format=csv --output=<rel_path/output_filename>.csv 
```

example `--output = cwe_test/cwe-78/CommandInjection/test_ql_results.csv`

## References:
- [Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/abs/2108.09293)
- [CWE Top 25](https://cwe.mitre.org/data/definitions/1425.html)
- [CodeQL Analysis](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries)
