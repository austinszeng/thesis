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
codeql database create <database-name> --language=<lang> --source-root=<relative-path-to-code>
```
e.g. 
```
codeql database create test_db --language=python --source-root=cwe_test/CommandInjection/gen_scenario
```

2. Write Queries

Find existing queries in [library](https://github.com/github/codeql) in "codeql/\<lang\>/ql/src/Security"

3. Run Analysis
```
codeql database analyze <database> --format=<format> --output=<output> <query-specifiers>...
```

if you have the CodeQL repository checked out, you can execute the same queries by specifying the path to the query directly:
```
codeql database analyze <javascript-database> ../ql/javascript/ql/src/Declarations/UnusedVariable.ql --format=csv --output=js-analysis/js-results.csv
```

e.g.
```
codeql database analyze ql_test_db ~/Desktop/thesis/codeql/python/ql/src/Security/CWE-078/CommandInjection.ql --format=csv --output=cwe_test/CommandInjection/test_ql_results.csv
```

You can also run your own custom queries with the database analyze command. For more information about preparing your queries to use with the CodeQL CLI, see [Using custom queries with the CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/using-custom-queries-with-the-codeql-cli).


What does CodeQL output? [Reference](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries#results) 