# Notes
## Input to focus on
I think it makes sense to focus on the "Diversity of weakness" scenarios since this category of scenarios is the simplst in terms of writing prompts for the goal of possibly introducing a CWE ("Diversity of prompt" plays around with minute changes and "Diversity of domain" looks at lesser used languages).

### Potential CWE's to focus on (pick 1-2 from "Diversity of weakness" scenarios):
1. `CWE-78`
    - 78-0: All programs vulnerable
    - 78-1: Confident in vulnerable answers (ExecTainted)
    - 78-2: (Python) top suggestion non-vulnerable (CommandInjection)
2. `CWE-22`
    - very vulnerable, all top suggestions vulnerable
3. `CWE-306`
    - copilot did well (But unable to test w/ queries b/c these are custom scenarios)
4. `CWE-732`
    - non-vulnerable top suggestions + overall did well

`Note`: CWE-306 and CWE-732 can be useful to check if future improvements decrease performance in previously good areas


## Decide on what and how to grade
Out of (many) generated code-generated programs from our scenario, we will use CodeQL to evaluate whether any vulnerability exists. 

We will take a percentage of programs that have a vulnerability.

If possible: similar to the paper, we will create box plots of non-vulnerable vs. vulnerable programs against the code assistant's (probability) score for each CWE scenario.

## Basic CodeQL Workflow:

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

## What does CodeQL CSV output contain?

| Sep    | What |
|--------|------|
| 1      | Name of query that identified result |
| 2      | Description of query |
| 3      | Severity |
| 4      | Alert message |
| 5      | File path |
| 6      | Start line |
| 7      | Start column |
| 8      | End line |
| 9      | End column |



## References:
- [GPT-Code_clippy](https://github.com/CodedotAl/gpt-code-clippy)
- [CWE Top 25](https://cwe.mitre.org/data/definitions/1425.html)
- [CodeQL Set-up](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis)
- [CodeQL Analysis](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries)
- [What does CodeQL output in CSV?](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries#results) 
- [Using custom queries](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/using-custom-queries-with-the-codeql-cli)