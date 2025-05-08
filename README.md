# N-Gram Language Model for Sentence Probability Calculation

## Overview
This Python script implements an N-Gram Language Model to calculate the probability of a sentence based on the frequency of n-grams (sequences of words) in a given corpus. It uses natural language processing techniques such as tokenization, lemmatization, and stemming to process the input text before generating n-grams. The probability of a sentence is then calculated using these n-grams.

The script is designed to handle Persian text and uses the **Hazm** library for tokenization, normalization, lemmatization, and stemming.

## Requirements
- Python 3.x
- **Libraries**:
  - `nltk`: for n-gram generation and word tokenization.
  - `hazm`: for Persian language processing tasks such as normalization, lemmatization, and stemming.
  - `collections`: for handling frequency counts of n-grams.
  - `re`: for regular expressions to clean the input data.
