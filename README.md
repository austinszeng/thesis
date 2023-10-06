# Austin Zeng's Senior Thesis Fall 2023 - Spring 2024

## Overview
### Vulnerability Evaluation of Recommender Systems (Code Assistant)
Following [Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/pdf/2108.09293.pdf).

This work is located in the `copilot-eval` folder.

References/Tools:
- [GPT-Code_clippy](https://github.com/CodedotAl/gpt-code-clippy)
- [GitHub CodeQL](https://github.com/github/vscode-codeql-starter/)
- [CWE Top 25](https://cwe.mitre.org/data/definitions/1425.html)

Potential CWE's to focus on (pick 1-2 from "Diversity of weakness" scenarios):
1. CWE-78
    - 78-0: All programs vulnerable
    - 78-1: Confident in vulnerable answers
    - 78-2: (Python) top suggestion non-vulnerable
2. CWE-22
    - very vulnerable, all top suggestions vulnerable
3. CWE-306
    - copilot did well
4. CWE-732
    - non-vulnerable top suggestions + overall did well

Note: CWE-306 and CWE-732 can be useful to check if future improvements decrease performance in previously good areas


# misc
Diversity of weakness (dow) : performance when prompted with diff scenarios where completion could introduce a software CWE. each CWE --> 3 diff scenarios

Diversity of prompt (dop) : how performance changes for a speicifc CWE, given small changes to the provided prompt

### Improvement using (Unlearning Methods?)