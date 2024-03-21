# Senior Thesis (Fall 2023 - Spring 2024)

## Overview
Repository to organize my thesis work investigating whether vulnerabilities in code generation by ML-models can be improved by unlearning algorithms. The project can roughly be split into two parts: 
1. Creating a testing framework to measure the code generation performance of ML-models
2. Apply unlearning algorithm on ML-model and run analysis on the before and after results given vulnerability and quality metrics.

Uses [copilot-cwe-scenarios-dataset](https://zenodo.org/records/5225651) for CWE scenarios and associated queries.

## Vulnerability Evaluation of Recommender Systems
Following [Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/pdf/2108.09293.pdf).

This work is located in the `copilot-eval` folder.

## Improvement using Unlearning Algorithms
[Knowledge Unlearning](https://arxiv.org/abs/2210.01504)