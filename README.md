# Python Code Efficiency Analyzer

This project is a tool designed to benchmark and evaluate code performance and time complexity (Big O notation). 

## 🎯 Purpose
In AI Training and Model Evaluation, choosing the most efficient algorithm is crucial. This script demonstrates my ability to analyze Python code, identify performance bottlenecks (like O(n²) complexity), and implement optimized solutions using data structures like Sets (O(n) complexity).

## 🚀 How it Works
The script generates a large dataset (15,000 items) and compares two different approaches to solve the same problem (finding duplicate elements):
1. **Approach A (Inefficient):** Uses `.count()` inside a nested-like loop structure, causing an O(n²) time complexity.
2. **Approach B (Optimized):** Uses Hash Sets to track elements in a single pass, achieving O(n) time complexity.

## 📊 Sample Output Results
```text
Iniciando teste de eficiência algoritmo...

Tempo da abordagem lenta O(n²): 1.42510 segundos
Tempo da abordagem rápida O(n): 0.00112 segundos

A abordagem otimizada foi 1272.4x mais rápida!
```

## 🛠️ Skills Demonstrated
* Algorithm Optimization & Time Complexity (Big O)
* Python Data Structures (Lists, Sets)
* Benchmarking and Code Auditing
* Code Quality Evaluation
