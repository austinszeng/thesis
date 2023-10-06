# Notes
## Input to focus on
I think it makes sense to focus on the "Diversity of weakness" scenarios since this category of scenarios is the simplst in terms of writing prompts for the goal of possibly introducing a software CWE. ["Diversity of prompt" plays around with minute changes and "Diversity of domain" looks at lesser used languages.]

## Appropriate scenarios + tools for input
[Information on setting up CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli)

## Decide on what and how to grade
Out of (many) generated Copilot programs from our scenario, we will use CodeQL to evaluate whether any vulnerability exists. 

We will take a percentage of programs that have a vulnerability. 

Similar to the paper, we will create box plots of non-vulnerable vs. vulnerable programs against Copilot's (probability) score for each CWE scenario

## Basic CodeQL Workflow:
Reference:
- [Set-up](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/preparing-your-code-for-codeql-analysis)
- [Analysis](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries)

1. Create Database:

```
codeql database create <database-name> --language=<lang> --source-root=<path-to-code>
```
2. Write Queries

Find existing queries in [library](https://github.com/github/codeql) in "codeql/\<lang\>/ql/src/Security" or write custom queries (`.q1`)

3. Run Analysis
```
codeql database analyze <database-name> --query=<path-to-query> --format=sarif-latest
```