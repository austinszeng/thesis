# Notes
## Input to focus on
I think it makes sense to focus on the "Diversity of weakness" scenarios since this category of scenarios is the simplst in terms of writing prompts for the goal of possibly introducing a CWE. ["Diversity of prompt" plays around with minute changes and "Diversity of domain" looks at lesser used languages.]

## Appropriate scenarios + tools for input
[Information on setting up CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli)

## Decide on what and how to grade
Out of (many) generated Copilot programs from our scenario, we will use CodeQL to evaluate whether any vulnerability exists. 

We will take a percentage of programs that have a vulnerability. 

Similar to the paper, we will create box plots of non-vulnerable vs. vulnerable programs against Copilot's (probability) score for each CWE scenario

## Basic CodeQL Workflow:

1. Create Database:

Database should be created for each CWE scenario group of the Copilot generated programs.

```
codeql database create <database-name> --language=<lang> --source-root=<relative-path-to-code>
```
e.g. 
```
codeql database create test_db --language=python --source-root=cwe_test/CommandInjection/gen_scenario
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

example `--output=cwe_test/CommandInjection/test_ql_results.csv`


References:
- [Set-up](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis)
- [Analysis](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries)
- [What does CodeQL output in CSV?](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries#results) 
- [Using custom queries](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/using-custom-queries-with-the-codeql-cli)