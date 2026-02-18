# SQuAD 2.0 Trials Log

This file tracks all trial runs to monitor improvements and avoid over-correction.

---

## Baseline Test - Sample Results
**Timestamp:** 2026-02-07 18:04:07

**Dataset:** data/squad2.0-dev-1000-sample-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 51.00 |
| **NoAns Accuracy** | 78.26% (18/23) |
| **HasAns F1** | 27.78 |
| **HasAns EM** | 25.93 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |

---

## dev_trial_tiny_202602071853
**Timestamp:** 2026-02-07 18:53:29

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |

## dev_trial_tiny_202602071903
**Timestamp:** 2026-02-07 19:03:32

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |

### Detailed Results

| CSV Line | Question | Actual Answer | Model Prediction | Status |
|----------|----------|---------------|------------------|--------|
| 2 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 3 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 4 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 5 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 6 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 7 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 8 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 9 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 10 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1. | ❌ |
| 11 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 12 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 13 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602071914
**Timestamp:** 2026-02-07 19:14:53

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |

### Detailed Results

| CSV Line | Question | Actual Answer | Model Prediction | Status |
|----------|----------|---------------|------------------|--------|
| 2 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 3 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 4 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 5 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 6 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 7 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 8 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 9 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 10 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1. | ❌ |
| 11 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 12 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 13 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602071926
**Timestamp:** 2026-02-07 19:26:10

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |

### Detailed Results

| CSV Line | Question | Actual Answer | Model Prediction | Status |
|----------|----------|---------------|------------------|--------|
| 2 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 3 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 4 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 5 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 6 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 7 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 8 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 9 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 10 | What are the two integer responses to a decision p... | 1 or 0 | 1 and 0 | ❌ |
| 11 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 12 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 13 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602071932
**Timestamp:** 2026-02-07 19:32:43

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |

### Detailed Results

| CSV Line | Question | Actual Answer | Model Prediction | Status |
|----------|----------|---------------|------------------|--------|
| 2 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 3 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 4 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 5 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 6 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 7 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 8 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 9 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 10 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1. | ❌ |
| 11 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 12 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 13 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602071958
**Timestamp:** 2026-02-07 19:58:16

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 55.56 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 33.33 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |

### Detailed Results

| CSV Line | Question | Actual Answer | Model Prediction | Status |
|----------|----------|---------------|------------------|--------|
| 2 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 3 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 4 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 5 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 6 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 7 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 8 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 9 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 10 | What are the two integer responses to a decision p... | 1 or 0 | NO ANSWER | ❌ |
| 11 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 12 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 13 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602072014
**Timestamp:** 2026-02-07 20:14:52

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |

### Detailed Results

| CSV Line | Question | Actual Answer | Model Prediction | Status |
|----------|----------|---------------|------------------|--------|
| 2 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 3 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 4 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 5 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 6 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 7 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 8 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 9 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 10 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1. | ❌ |
| 11 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 12 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 13 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602072032
**Timestamp:** 2026-02-07 20:32:19

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 66.67% (8/12) |

### Detailed Results

| CSV Line | Question | Actual Answer | Model Prediction | Status |
|----------|----------|---------------|------------------|--------|
| 2 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 3 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 4 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 5 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 6 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 7 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 8 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 9 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 10 | What are the two integer responses to a decision p... | 1 or 0 | 1 and 0 | ❌ |
| 11 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 12 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 13 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

**correct binary classification:** 66.67% (8/12)

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602072124
**Timestamp:** 2026-02-07 21:24:43

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 66.67% (8/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 4 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 6 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1 and 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

**correct binary classification:** 66.67% (8/12)

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602072125
**Timestamp:** 2026-02-07 21:25:49

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 100.00% (4/4) |
| **HasAns F1** | 41.67 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 66.67% (8/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 4 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 6 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1. | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

**correct binary classification:** 66.67% (8/12)

⚠️ **WARNING: Potential Over-correction Detected!**
High NoAns accuracy but low HasAns F1 suggests the model is too conservative.

---

## dev_trial_tiny_202602072140
**Timestamp:** 2026-02-07 21:40:28

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 50.23 |
| **NoAns Accuracy** | 50.00% (2/4) |
| **HasAns F1** | 50.35 |
| **HasAns EM** | 37.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | The set of triples (a, b, c) such that the relation a × b = c holds is the set of | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... |  ANSWER | NO ANSWER | ✅ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of proNOblems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | The size of the input is usually taken to be the size of the input in bits. | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | A monthly subscription. | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, the answer is 0 and 1. | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL (Los Angeles Rams, San Diego Chargers); | ❌ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | The Mojave Desert. | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## dev_trial_tiny_202602131702
**Timestamp:** 2026-02-13 17:03:02

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 25.00 |
| **Overall F1** | 37.50 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 43.75 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 66.67% (8/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | set of triples (a, b, c) such that the relation a × b = c holds is the set of | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sky Q Mini set top boxes connect to the Sky Q Silver set top boxes with a Wi-Fi or Power-line connection rather | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | set of problems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | 2007 | ❌ |
| 6 | In what unit is the size of the input measured? | bits | size of the input is usually taken to be the size of the input in bits. | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | monthly subscription. | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | answer is 1 and 0. | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | (Los Angeles Rams, San Diego Chargers); | ❌ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert. | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | Tehachapi Mountains. | ❌ |

**correct binary classification:** 66.67% (8/12)

---

## dev_trial_tiny_202602131724
**Timestamp:** 2026-02-13 17:24:23

**Dataset:** DataFrame

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 58.33 |
| **Overall F1** | 59.52 |
| **NoAns Accuracy** | 75.00% (3/4) |
| **HasAns F1** | 51.79 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 66.67% (8/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | The set of triples (a, b, c) such that the relation a × b = c holds. | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 4 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | The size of the input is usually taken to be the size of the input in bits. | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | NO ANSWER | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | ❌ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | The Mojave Desert. | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 66.67% (8/12)

---

## qa_bench_50_202602131800
**Timestamp:** 2026-02-13 18:00:38

**Dataset:** DataFrame

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 48.00 |
| **Overall F1** | 55.00 |
| **NoAns Accuracy** | 60.00% (12/20) |
| **HasAns F1** | 51.66 |
| **HasAns EM** | 40.00 |
| **Total Questions** | 50 (HasAns: 30, NoAns: 20) |
| **Binary Classification** | 70.00% (35/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | what other digital TV service took Sky UK Limited'... | Freeview | Freeview | ✅ |
| 1 | What states that only problems that cannot be solv... | NO ANSWER | The Cobham–Edmonds thesis. | ❌ |
| 2 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | NO ANSWER | ✅ |
| 3 | What is a typical type of computational problem wh... | NO ANSWER | NO ANSWER | ✅ |
| 4 | Is a problem instance typically characterized as a... | concrete | According to the given problem, a problem instance is referred to as a " rather concrete utterance" | ❌ |
| 5 | What business districts are within the downtown Lo... | NO ANSWER | The Downtown Los Angeles central business district as well as those lining the Wilshire Boulevard Miracle Mile including Century City, Westwood and | ❌ |
| 6 | Who was the chief executive officer when the servi... | Sam Chisholm | Sam Chisholm | ✅ |
| 7 | What was the name of Bohemond's nephew? | Tancred | Tancred. | ❌ |
| 8 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 9 | If P = NP is unsolved, and reduction is applied to... | there is no known polynomial-time solution | If P = NP is not solved, and a known NP-complete problem Π2 is reduced to Π1, then no polynomial | ❌ |
| 10 | What answer denotes that an algorithm has accepted... | yes | yes | ✅ |
| 11 | What are the two integer responses to a decision p... | 1 or 0 | NO ANSWER | ❌ |
| 12 | What complexity class do incompatible problems of ... | NO ANSWER | co-NP | ❌ |
| 13 | In what expression can one expect to find DTIME(n) | DTIME(n2) | NO ANSWER | ❌ |
| 14 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 15 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |
| 16 | What are the least well known complexity resources... | NO ANSWER | NO ANSWER | ✅ |
| 17 | What year did BSkyB and Virgin Media have an agree... | NO ANSWER | NO ANSWER | ✅ |
| 18 | What channels were always available on the network... | NO ANSWER | NO ANSWER | ✅ |
| 19 | Is the output of a functional problem typically ch... | complex | NO ANSWER | ❌ |
| 20 | Resources are constrained by hierarchy theorems to... | a proper hierarchy on the classes defined | resources. | ❌ |
| 21 | What kind of economy did northern California start... | tech-oriented | A tech-oriented economy. | ❌ |
| 22 | What type of landscapes other than geologic and na... | topographic | NO ANSWER | ❌ |
| 23 | What company was never involved with NDS? | NO ANSWER | NO ANSWER | ✅ |
| 24 | What is the expression set called where three inte... | NO ANSWER | The set of triples (a, b, c) such that the relation a × b = c holds. | ❌ |
| 25 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 26 | What year were farmlands turned into suburbs? | NO ANSWER | NO ANSWER | ✅ |
| 27 | What is the most commonplace model utilized in com... | the Turing machine | The Turing machine is the most commonly used model in complexity theory. | ❌ |
| 28 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 29 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 30 | Within the 30 days how many digiboxes had been sol... | 100,000 | Within 30 days, over 100,000 digiboxes had been sold. | ❌ |
| 31 | What satellite was used when Sky digital was launc... | Astra 2A | Astra 2A | ✅ |
| 32 | Who began a program of church reform in the 1100s | NO ANSWER | The dukes of Normandy. | ❌ |
| 33 | In what unit is the size of the input measured? | bits | The size of the input is usually taken to be the size of the input in bits. | ❌ |
| 34 | The two listed teams play for which NCAA group? | Division I | The Pac-12 Conference. | ❌ |
| 35 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 36 | What are four examples of problems believed to be ... | NO ANSWER | The graph isomorphism problem, the discrete logarithm problem and the integer factorization problem are examples of problems believed to be | ❌ |
| 37 | What type of groups divides California into only n... | NO ANSWER | AAA Auto Clubs. | ❌ |
| 38 | What year was Setanta Sports awarded Primeier Leag... | 2006 | 2006 | ✅ |
| 39 | What war occured in the 1oth century? | NO ANSWER | NO ANSWER | ✅ |
| 40 | AC and NC are complexity classes typically associa... | Boolean | Boolean | ✅ |
| 41 | Who used the church to unify themselves? | dukes | The dukes of Normandy. | ❌ |
| 42 | What encoding decision needs to be made in order t... | how graphs are encoded as binary strings | NO ANSWER | ❌ |
| 43 | What computational problem is not commonly associa... | NO ANSWER | NO ANSWER | ✅ |
| 44 | What famous snowbaorder lives in southern Californ... | Shaun White | Shaun White | ✅ |
| 45 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 46 | What isn't required by customers to get Sky+ funct... | NO ANSWER | A monthly fee. | ❌ |
| 47 | How many campuses does the California State Univer... | 12 | 12 | ✅ |
| 48 | What is an example of a problem that rests within ... | Boolean satisfiability problem | The Boolean satisfiability problem, the Hamiltonian path problem, and the vertex cover problem are the problems that are known to also | ❌ |
| 49 | What company has veto over the presence of channel... | NO ANSWER | NO ANSWER | ✅ |

**correct binary classification:** 70.00% (35/50)

---

## official_50_sample_202602132058
**Timestamp:** 2026-02-13 20:58:20

**Dataset:** DataFrame

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 44.00 |
| **Overall F1** | 49.49 |
| **NoAns Accuracy** | 56.52% (13/23) |
| **HasAns F1** | 43.50 |
| **HasAns EM** | 33.33 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |
| **Binary Classification** | 66.00% (33/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What isn't required by customers to get Sky+ funct... | NO ANSWER | A monthly fee. | ❌ |
| 2 | What thesis specifies that a trinomial relationshi... | NO ANSWER | Cobham-Edmonds thesis | ❌ |
| 3 | What company owns ACB? | NO ANSWER | The Walt Disney Company | ❌ |
| 4 | Southern California's distinctive regions are divi... | economically | polit economically | ❌ |
| 5 | Who was given the highlights of most of the matche... | BBC | The BBC was given the highlights of most of the matches. | ❌ |
| 6 | Who was Richard's fiancee? | Berengaria | Berengaria | ✅ |
| 7 | What is the expression used to identify any given ... | DTIME(f(n)) | DTTIME(f(n)). | ❌ |
| 8 | What are three examples of complexity classes asso... | BPP, ZPP and RP | BPP, ZPP, and RP. | ❌ |
| 9 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | ✅ |
| 10 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | ✅ |
| 11 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | ✅ |
| 12 | What kind of university is the California Institut... | private | The California Institute of Technology is a private (NO, the California Institute of Technology is private, the California Institute of Technology is | ❌ |
| 13 | A complexity resource can also be described as wha... | computational resource | NO ANSWER | ❌ |
| 14 | Point Conception is an example of a landmark among... | northern | Point Conception is a boundary of southern California. | ❌ |
| 15 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | NO ANSWER | ✅ |
| 16 | Sky UK Limited is now known by what name? | NO ANSWER | Sky UK Limited (formerly British Sky Broadcasting or BSkyB) | ❌ |
| 17 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | ✅ |
| 18 | Where did the Normans carve out a principality bef... | NO ANSWER | NO ANSWER | ✅ |
| 19 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | S Sant'Eufemia | ❌ |
| 20 | What year did Richards fleet avoid a storm? | NO ANSWER | 1191 | ❌ |
| 21 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | ✅ |
| 22 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems. | ❌ |
| 23 | What are the other four important complexity class... | NO ANSWER | The BPP, ZPP, RP, AC, NC, BQP, and QMA. | ❌ |
| 24 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | ✅ |
| 25 | How many California University campuses are there? | NO ANSWER | There is a 5 University of California campuses and 12 California State University campuses. | ❌ |
| 26 | How many customaries does Norman customary law hav... | two | NO ANSWER | ❌ |
| 27 | What are two fields of theoretical computer scienc... | NO ANSWER | NO ANSWER | ✅ |
| 28 | What is the metric they use to determine how busy ... | passenger volume | NO ANSWER | ❌ |
| 29 | What culture's arrival in Scotland is know as the ... | Norman | Normans | ❌ |
| 30 | What company was formed by the merger of Sky Telev... | BSkyB | BSkyB | ✅ |
| 31 | Southern California's economy can be described as ... | diverse | NO ANSWER | ❌ |
| 32 | In the definition based off the mountain range, wh... | southern | The desert portions of north Los Angeles County would be included in the southern California region. | ❌ |
| 33 | Where is Redland University located? | NO ANSWER | NO ANSWER | ✅ |
| 34 | What is the integer practice problem? | NO ANSWER | NO ANSWER | ✅ |
| 35 | What main business district is in downtown Los Ang... | NO ANSWER | D Downtown Los Angeles central business district | ❌ |
| 36 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | ✅ |
| 37 | What is the softest problem in C? | NO ANSWER | NO ANSWER | ✅ |
| 38 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | They share recordings and other media. | ❌ |
| 39 | A specific algorithm demonstrating T(n) represents... | upper bound | NO ANSWER | ❌ |
| 40 | Complexity theory classifies problems based on wha... | difficulty | problems based on their difficulty | ❌ |
| 41 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | ✅ |
| 42 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County, Santa Maria and San Luis Obispo areas. | ❌ |
| 43 | What is the population of the second largest city ... | 1.3 million | 1.3 million | ✅ |
| 44 | Case complexities provide three likelihoods of wha... | inputs | NO ANSWER | ❌ |
| 45 | What kind of universities is the region famous for... | research | public and private institutions | ❌ |
| 46 | What is a growing sport in southern California? | Rugby | Rugby | ✅ |
| 47 | What is a typical type of computational problem wh... | NO ANSWER | NO ANSWER | ✅ |
| 48 | What is an example of a measurement within a compl... | computation time | NO ANSWER | ❌ |
| 49 | The legislation allowed California to be admitted ... | free | free state | ❌ |

**correct binary classification:** 66.00% (33/50)

---

## official_50_sample_202602132134
**Timestamp:** 2026-02-13 21:34:13

**Dataset:** dev-data/official_50_sample-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 46.00 |
| **Overall F1** | 52.75 |
| **NoAns Accuracy** | 60.87% (14/23) |
| **HasAns F1** | 45.83 |
| **HasAns EM** | 33.33 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |
| **Binary Classification** | 68.00% (34/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What isn't required by customers to get Sky+ funct... | NO ANSWER | A monthly fee. | ❌ |
| 2 | What thesis specifies that a trinomial relationshi... | NO ANSWER | The Cobham-Edmonds thesis states that "the time complexities in any two reasonable and general models of computation are polynomially | ❌ |
| 3 | What company owns ACB? | NO ANSWER | The Walt Disney Company | ❌ |
| 4 | Southern California's distinctive regions are divi... | economically | polit economically | ❌ |
| 5 | Who was given the highlights of most of the matche... | BBC | The BBC was given the highlights of most of the matches. | ❌ |
| 6 | Who was Richard's fiancee? | Berengaria | Berengaria | ✅ |
| 7 | What is the expression used to identify any given ... | DTIME(f(n)) | The answer is DTIME(f(n)). | ❌ |
| 8 | What are three examples of complexity classes asso... | BPP, ZPP and RP | BPP, ZPP, and RP. | ❌ |
| 9 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | ✅ |
| 10 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | ✅ |
| 11 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk, Rob Machado, Tim Curran, Bobby Martinez, Pat O'Connell, Dane Reynolds, and Chris Ward | ❌ |
| 12 | What kind of university is the California Institut... | private | Private | ✅ |
| 13 | A complexity resource can also be described as wha... | computational resource | NO ANSWER | ❌ |
| 14 | Point Conception is an example of a landmark among... | northern | Point Conception is a boundary of southern California. | ❌ |
| 15 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | NO ANSWER | ✅ |
| 16 | Sky UK Limited is now known by what name? | NO ANSWER | NO ANSWER | ✅ |
| 17 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | ✅ |
| 18 | Where did the Normans carve out a principality bef... | NO ANSWER | NO ANSWER | ✅ |
| 19 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | S Sant'Eufemia | ❌ |
| 20 | What year did Richards fleet avoid a storm? | NO ANSWER | The fleet left Messina in April 1191. | ❌ |
| 21 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | ✅ |
| 22 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems. | ❌ |
| 23 | What are the other four important complexity class... | NO ANSWER | The BPP, ZPP, RP, AC, NC, BQP, and QMA. | ❌ |
| 24 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | ✅ |
| 25 | How many California University campuses are there? | NO ANSWER | There is a 5 University of California campuses and 12 California State University campuses. | ❌ |
| 26 | How many customaries does Norman customary law hav... | two | NO ANSWER | ❌ |
| 27 | What are two fields of theoretical computer scienc... | NO ANSWER | NO ANSWER | ✅ |
| 28 | What is the metric they use to determine how busy ... | passenger volume | NO ANSWER | ❌ |
| 29 | What culture's arrival in Scotland is know as the ... | Norman | Normans | ❌ |
| 30 | What company was formed by the merger of Sky Telev... | BSkyB | BSkyB | ✅ |
| 31 | Southern California's economy can be described as ... | diverse | NO ANSWER | ❌ |
| 32 | In the definition based off the mountain range, wh... | southern | The desert portions of north Los Angeles County would be included in the southern California region. | ❌ |
| 33 | Where is Redland University located? | NO ANSWER | NO ANSWER | ✅ |
| 34 | What is the integer practice problem? | NO ANSWER | NO ANSWER | ✅ |
| 35 | What main business district is in downtown Los Ang... | NO ANSWER | The Downtown Los Angeles central business district. | ❌ |
| 36 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | ✅ |
| 37 | What is the softest problem in C? | NO ANSWER | NO ANSWER | ✅ |
| 38 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | They share recordings and other media. | ❌ |
| 39 | A specific algorithm demonstrating T(n) represents... | upper bound | NO ANSWER | ❌ |
| 40 | Complexity theory classifies problems based on wha... | difficulty | problems based on their difficulty | ❌ |
| 41 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | ✅ |
| 42 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County, Santa Maria and San Luis Obispo areas. | ❌ |
| 43 | What is the population of the second largest city ... | 1.3 million | 1.3 million | ✅ |
| 44 | Case complexities provide three likelihoods of wha... | inputs | NO ANSWER | ❌ |
| 45 | What kind of universities is the region famous for... | research | The region is the Tech Coast and is the region is the Tech Coast, and is the region is the Tech Coast, and | ❌ |
| 46 | What is a growing sport in southern California? | Rugby | Rugby | ✅ |
| 47 | What is a typical type of computational problem wh... | NO ANSWER | NO ANSWER | ✅ |
| 48 | What is an example of a measurement within a compl... | computation time | NO ANSWER | ❌ |
| 49 | The legislation allowed California to be admitted ... | free | free state | ❌ |

**correct binary classification:** 68.00% (34/50)

---

## official_50_sample_202602150036
**Timestamp:** 2026-02-15 00:36:13

**Parameters:** prob_threshold=0.05, bias_value=20.0

**Dataset:** dev-data/official_50_sample-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 52.00 |
| **Overall F1** | 57.38 |
| **NoAns Accuracy** | 47.83% (11/23) |
| **HasAns F1** | 65.52 |
| **HasAns EM** | 55.56 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |
| **Binary Classification** | 74.00% (37/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What isn't required by customers to get Sky+ funct... | NO ANSWER | a monthly fee | ❌ |
| 2 | What thesis specifies that a trinomial relationshi... | NO ANSWER | Cobham-Edmonds thesis | ❌ |
| 3 | What company owns ACB? | NO ANSWER | The Walt Disney Company | ❌ |
| 4 | Southern California's distinctive regions are divi... | economically | e economically | ❌ |
| 5 | Who was given the highlights of most of the matche... | BBC | The BBC | ❌ |
| 6 | Who was Richard's fiancee? | Berengaria | Berengaria | ✅ |
| 7 | What is the expression used to identify any given ... | DTIME(f(n)) | DTIME(f(n)). | ❌ |
| 8 | What are three examples of complexity classes asso... | BPP, ZPP and RP | BPP, ZPP, RP | ❌ |
| 9 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | ✅ |
| 10 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | ✅ |
| 11 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | ✅ |
| 12 | What kind of university is the California Institut... | private | Private | ✅ |
| 13 | A complexity resource can also be described as wha... | computational resource | communication | ❌ |
| 14 | Point Conception is an example of a landmark among... | northern | Point Conception | ❌ |
| 15 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | NO ANSWER | ✅ |
| 16 | Sky UK Limited is now known by what name? | NO ANSWER | Sky UK Limited (formerly British Sky Broadcasting or BSkyB) | ❌ |
| 17 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | ✅ |
| 18 | Where did the Normans carve out a principality bef... | NO ANSWER | Antioch | ❌ |
| 19 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | Sant'Eufemia | ❌ |
| 20 | What year did Richards fleet avoid a storm? | NO ANSWER | 1191 | ❌ |
| 21 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | ✅ |
| 22 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems. | ❌ |
| 23 | What are the other four important complexity class... | NO ANSWER | BPP, ZPP, RP, AC, NC, BQP, QMA | ❌ |
| 24 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | ✅ |
| 25 | How many California University campuses are there? | NO ANSWER | 19 | ❌ |
| 26 | How many customaries does Norman customary law hav... | two | 2 | ❌ |
| 27 | What are two fields of theoretical computer scienc... | NO ANSWER | NO ANSWER | ✅ |
| 28 | What is the metric they use to determine how busy ... | passenger volume | passenger volume | ✅ |
| 29 | What culture's arrival in Scotland is know as the ... | Norman | Normans | ❌ |
| 30 | What company was formed by the merger of Sky Telev... | BSkyB | BSkyB | ✅ |
| 31 | Southern California's economy can be described as ... | diverse | heavily dependent | ❌ |
| 32 | In the definition based off the mountain range, wh... | southern | the southern | ❌ |
| 33 | Where is Redland University located? | NO ANSWER | NO ANSWER | ✅ |
| 34 | What is the integer practice problem? | NO ANSWER | NO ANSWER | ✅ |
| 35 | What main business district is in downtown Los Ang... | NO ANSWER | D Downtown Los Angeles | ❌ |
| 36 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | ✅ |
| 37 | What is the softest problem in C? | NO ANSWER | NO ANSWER | ✅ |
| 38 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | share recordings and other media | ❌ |
| 39 | A specific algorithm demonstrating T(n) represents... | upper bound | Upper bound | ✅ |
| 40 | Complexity theory classifies problems based on wha... | difficulty | their difficulty | ❌ |
| 41 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | ✅ |
| 42 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County, Santa Maria and San Luis Obispo areas. | ❌ |
| 43 | What is the population of the second largest city ... | 1.3 million | 1.3 million | ✅ |
| 44 | Case complexities provide three likelihoods of wha... | inputs | time | ❌ |
| 45 | What kind of universities is the region famous for... | research | Public and private institutions | ❌ |
| 46 | What is a growing sport in southern California? | Rugby | Rugby | ✅ |
| 47 | What is a typical type of computational problem wh... | NO ANSWER | Decision problem | ❌ |
| 48 | What is an example of a measurement within a compl... | computation time | NO ANSWER | ❌ |
| 49 | The legislation allowed California to be admitted ... | free | free state | ❌ |

**correct binary classification:** 74.00% (37/50)

---

## official_50_sample_202602162222
**Timestamp:** 2026-02-16 22:22:12

**Parameters:** prob_threshold=0.05, bias_value=20.0

**Dataset:** dev-data/official_50_sample-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 48.00 |
| **Overall F1** | 54.98 |
| **NoAns Accuracy** | 43.48% (10/23) |
| **HasAns F1** | 64.78 |
| **HasAns EM** | 51.85 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |
| **Binary Classification** | 72.00% (36/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What isn't required by customers to get Sky+ funct... | NO ANSWER | monthly fee | ❌ |
| 2 | What thesis specifies that a trinomial relationshi... | NO ANSWER | Cobham-Edmonds thesis | ❌ |
| 3 | What company owns ACB? | NO ANSWER | Walt Disney Company | ❌ |
| 4 | Southern California's distinctive regions are divi... | economically | economically | ✅ |
| 5 | Who was given the highlights of most of the matche... | BBC | BBC | ✅ |
| 6 | Who was Richard's fiancee? | Berengaria | Berengaria | ✅ |
| 7 | What is the expression used to identify any given ... | DTIME(f(n)) | DTTIME(f(n)) | ❌ |
| 8 | What are three examples of complexity classes asso... | BPP, ZPP and RP | BPP, ZPP, RP | ❌ |
| 9 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | ✅ |
| 10 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | ✅ |
| 11 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | ✅ |
| 12 | What kind of university is the California Institut... | private | Private | ✅ |
| 13 | A complexity resource can also be described as wha... | computational resource | communication | ❌ |
| 14 | Point Conception is an example of a landmark among... | northern | Point Conception | ❌ |
| 15 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | Ang Norman | ❌ |
| 16 | Sky UK Limited is now known by what name? | NO ANSWER | Sky UK Limited (formerly British Sky Broadcasting or BSkyB) | ❌ |
| 17 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | ✅ |
| 18 | Where did the Normans carve out a principality bef... | NO ANSWER | Antioch | ❌ |
| 19 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | Sant'Eufemia | ❌ |
| 20 | What year did Richards fleet avoid a storm? | NO ANSWER | 1191 | ❌ |
| 21 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | ✅ |
| 22 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems | ❌ |
| 23 | What are the other four important complexity class... | NO ANSWER | BPP, ZPP, RP, AC, NC, BQP, QMA | ❌ |
| 24 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | ✅ |
| 25 | How many California University campuses are there? | NO ANSWER | 19 | ❌ |
| 26 | How many customaries does Norman customary law hav... | two | 2 | ❌ |
| 27 | What are two fields of theoretical computer scienc... | NO ANSWER | NO ANSWER | ✅ |
| 28 | What is the metric they use to determine how busy ... | passenger volume | pass passenger volume | ❌ |
| 29 | What culture's arrival in Scotland is know as the ... | Norman | Normans | ❌ |
| 30 | What company was formed by the merger of Sky Telev... | BSkyB | BSkyB | ✅ |
| 31 | Southern California's economy can be described as ... | diverse | div diverse | ❌ |
| 32 | In the definition based off the mountain range, wh... | southern | southern | ✅ |
| 33 | Where is Redland University located? | NO ANSWER | NO ANSWER | ✅ |
| 34 | What is the integer practice problem? | NO ANSWER | NO ANSWER | ✅ |
| 35 | What main business district is in downtown Los Ang... | NO ANSWER | Downtown Los Angeles | ❌ |
| 36 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | ✅ |
| 37 | What is the softest problem in C? | NO ANSWER | NO ANSWER | ✅ |
| 38 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | share recordings and other media | ❌ |
| 39 | A specific algorithm demonstrating T(n) represents... | upper bound | upper | ❌ |
| 40 | Complexity theory classifies problems based on wha... | difficulty | difficulty | ✅ |
| 41 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | ✅ |
| 42 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County, Santa Maria and San Luis Obispo areas | ❌ |
| 43 | What is the population of the second largest city ... | 1.3 million | 1.3 million | ✅ |
| 44 | Case complexities provide three likelihoods of wha... | inputs | time | ❌ |
| 45 | What kind of universities is the region famous for... | research | Public and private institutions | ❌ |
| 46 | What is a growing sport in southern California? | Rugby | Rugby | ✅ |
| 47 | What is a typical type of computational problem wh... | NO ANSWER | decision problem | ❌ |
| 48 | What is an example of a measurement within a compl... | computation time | NO ANSWER | ❌ |
| 49 | The legislation allowed California to be admitted ... | free | free state | ❌ |

**correct binary classification:** 72.00% (36/50)

---

## tiny_dev_12_202602162242
**Timestamp:** 2026-02-16 22:42:37

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 33.33 |
| **Overall F1** | 36.67 |
| **NoAns Accuracy** | 75.00% (3/4) |
| **HasAns F1** | 17.50 |
| **HasAns EM** | 12.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 41.67% (5/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | They receive their own satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | NO ANSWER | ❌ |
| 6 | In what unit is the size of the input measured? | bits | NO ANSWER | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | and 1 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | NO ANSWER | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | NO ANSWER | ❌ |

**correct binary classification:** 41.67% (5/12)

---

## tiny_dev_12_202602162314
**Timestamp:** 2026-02-16 23:14:39

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 58.33 |
| **Overall F1** | 62.30 |
| **NoAns Accuracy** | 75.00% (3/4) |
| **HasAns F1** | 55.95 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | ✅ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | The size of the input is usually taken to be the size of the input in bits | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | ✅ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | Yes or no | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | Tehachapi Mountains | ✅ |

**correct binary classification:** 75.00% (9/12)

---

## official_50_sample_202602162339
**Timestamp:** 2026-02-16 23:39:12

**Dataset:** dev-data/official_50_sample-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 56.00 |
| **Overall F1** | 60.71 |
| **NoAns Accuracy** | 56.52% (13/23) |
| **HasAns F1** | 64.29 |
| **HasAns EM** | 55.56 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |
| **Binary Classification** | 72.00% (36/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What isn't required by customers to get Sky+ funct... | NO ANSWER | NO ANSWER | ✅ |
| 2 | What thesis specifies that a trinomial relationshi... | NO ANSWER | The Cobham-Edmonds thesis | ❌ |
| 3 | What company owns ACB? | NO ANSWER | The Walt Disney Company | ❌ |
| 4 | Southern California's distinctive regions are divi... | economically | economically | ✅ |
| 5 | Who was given the highlights of most of the matche... | BBC | The BBC | ❌ |
| 6 | Who was Richard's fiancee? | Berengaria | Berengaria | ✅ |
| 7 | What is the expression used to identify any given ... | DTIME(f(n)) | NO ANSWER | ❌ |
| 8 | What are three examples of complexity classes asso... | BPP, ZPP and RP | BPP, ZPP, RP | ❌ |
| 9 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | ✅ |
| 10 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | ✅ |
| 11 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | ✅ |
| 12 | What kind of university is the California Institut... | private | Private | ✅ |
| 13 | A complexity resource can also be described as wha... | computational resource | computational resource | ✅ |
| 14 | Point Conception is an example of a landmark among... | northern | Tehachapi Mountains | ❌ |
| 15 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | NO ANSWER | ✅ |
| 16 | Sky UK Limited is now known by what name? | NO ANSWER | Sky UK Limited (formerly British Sky Broadcasting or BSkyB) | ❌ |
| 17 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | ✅ |
| 18 | Where did the Normans carve out a principality bef... | NO ANSWER | NO ANSWER | ✅ |
| 19 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | Sant'Eufemia | ❌ |
| 20 | What year did Richards fleet avoid a storm? | NO ANSWER | April 1191 | ❌ |
| 21 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | ✅ |
| 22 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems | ❌ |
| 23 | What are the other four important complexity class... | NO ANSWER | BPP, ZPP, RP, AC, NC, BQP, QMA | ❌ |
| 24 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | ✅ |
| 25 | How many California University campuses are there? | NO ANSWER | 17 | ❌ |
| 26 | How many customaries does Norman customary law hav... | two | 2 | ❌ |
| 27 | What are two fields of theoretical computer scienc... | NO ANSWER | NO ANSWER | ✅ |
| 28 | What is the metric they use to determine how busy ... | passenger volume | NO ANSWER | ❌ |
| 29 | What culture's arrival in Scotland is know as the ... | Norman | The Norman culture | ❌ |
| 30 | What company was formed by the merger of Sky Telev... | BSkyB | BSkyB | ✅ |
| 31 | Southern California's economy can be described as ... | diverse | One of the largest | ❌ |
| 32 | In the definition based off the mountain range, wh... | southern | the southern | ❌ |
| 33 | Where is Redland University located? | NO ANSWER | NO ANSWER | ✅ |
| 34 | What is the integer practice problem? | NO ANSWER | NO ANSWER | ✅ |
| 35 | What main business district is in downtown Los Ang... | NO ANSWER | Downtown Los Angeles | ❌ |
| 36 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | ✅ |
| 37 | What is the softest problem in C? | NO ANSWER | NO ANSWER | ✅ |
| 38 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | allows all set top boxes in a household to share recordings and other media | ❌ |
| 39 | A specific algorithm demonstrating T(n) represents... | upper bound | NO ANSWER | ❌ |
| 40 | Complexity theory classifies problems based on wha... | difficulty | problems based on their difficulty | ❌ |
| 41 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | ✅ |
| 42 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County, Santa Maria and San Luis Obispo areas | ❌ |
| 43 | What is the population of the second largest city ... | 1.3 million | 1.3 million | ✅ |
| 44 | Case complexities provide three likelihoods of wha... | inputs | the time complexity | ❌ |
| 45 | What kind of universities is the region famous for... | research | public and private institutions | ❌ |
| 46 | What is a growing sport in southern California? | Rugby | Rugby | ✅ |
| 47 | What is a typical type of computational problem wh... | NO ANSWER | Decision problem | ❌ |
| 48 | What is an example of a measurement within a compl... | computation time | NO ANSWER | ❌ |
| 49 | The legislation allowed California to be admitted ... | free | free state | ❌ |

**correct binary classification:** 72.00% (36/50)

---

## tiny_dev_12_202602170017
**Timestamp:** 2026-02-17 00:17:23

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 58.33 |
| **Overall F1** | 61.11 |
| **NoAns Accuracy** | 50.00% (2/4) |
| **HasAns F1** | 66.67 |
| **HasAns EM** | 62.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 66.67% (8/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Margin | Status |
|-------|----------|---------------|------------------|--------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | 0.8517 | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | relation | 0.0071 | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | 0.0149 | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | They receive their own satellite feeds | -0.0730 | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | 0.0781 | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | -0.0720 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | -0.0164 | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | 0.0502 | ✅ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | yes or no | -0.2666 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | -0.1295 | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | -0.0223 | ✅ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | Tehachapi Mountains | 0.0000 | ✅ |

**correct binary classification:** 66.67% (8/12)

---

## official_50_sample_202602172257
**Timestamp:** 2026-02-17 22:57:19

**Dataset:** dev-data/official_50_sample-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 44.00 |
| **Overall F1** | 50.01 |
| **NoAns Accuracy** | 52.17% (12/23) |
| **HasAns F1** | 48.16 |
| **HasAns EM** | 37.04 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |
| **Binary Classification** | 68.00% (34/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Margin | Status |
|-------|----------|---------------|------------------|--------|--------|
| 0 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | 0.9298 | ✅ |
| 1 | What isn't required by customers to get Sky+ funct... | NO ANSWER | NO ANSWER | 0.1159 | ✅ |
| 2 | What thesis specifies that a trinomial relationshi... | NO ANSWER | The Cobham-Edmonds thesis | -0.0232 | ❌ |
| 3 | What company owns ACB? | NO ANSWER | The Walt Disney Company | -0.7912 | ❌ |
| 4 | Southern California's distinctive regions are divi... | economically | economically | -0.0558 | ✅ |
| 5 | Who was given the highlights of most of the matche... | BBC | The BBC was given the highlights of most of the matches | 0.0000 | ❌ |
| 6 | Who was Richard's fiancee? | Berengaria | Berengaria | 0.0000 | ✅ |
| 7 | What is the expression used to identify any given ... | DTIME(f(n)) | DN | -0.0056 | ❌ |
| 8 | What are three examples of complexity classes asso... | BPP, ZPP and RP | Other important complexity classes include BPP, ZPP and RP, | -0.1018 | ❌ |
| 9 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | 0.8663 | ✅ |
| 10 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | 0.6917 | ✅ |
| 11 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | 0.0000 | ✅ |
| 12 | What kind of university is the California Institut... | private | private | -0.0746 | ✅ |
| 13 | A complexity resource can also be described as wha... | computational resource | Analogous | -0.0738 | ❌ |
| 14 | Point Conception is an example of a landmark among... | northern | point | 0.0000 | ❌ |
| 15 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | NO ANSWER | 0.2174 | ✅ |
| 16 | Sky UK Limited is now known by what name? | NO ANSWER | British Sky Broadcasting or BSkyB | -0.4707 | ❌ |
| 17 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | 0.4528 | ✅ |
| 18 | Where did the Normans carve out a principality bef... | NO ANSWER | Antioch | -0.1325 | ❌ |
| 19 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | Sant'Eufemia | -0.0224 | ❌ |
| 20 | What year did Richards fleet avoid a storm? | NO ANSWER | April 1191 | -0.3875 | ❌ |
| 21 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | 0.5981 | ✅ |
| 22 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems | 0.0000 | ❌ |
| 23 | What are the other four important complexity class... | NO ANSWER | ZPP, AC, NC, and BQP | -0.1256 | ❌ |
| 24 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | -1.0000 | ✅ |
| 25 | How many California University campuses are there? | NO ANSWER | 17 | -0.0265 | ❌ |
| 26 | How many customaries does Norman customary law hav... | two | NO ANSWER | 0.0455 | ❌ |
| 27 | What are two fields of theoretical computer scienc... | NO ANSWER | NO ANSWER | 0.1195 | ✅ |
| 28 | What is the metric they use to determine how busy ... | passenger volume | NO ANSWER | 0.0196 | ❌ |
| 29 | What culture's arrival in Scotland is know as the ... | Norman | Normans | -0.6442 | ❌ |
| 30 | What company was formed by the merger of Sky Telev... | BSkyB | British Satellite Broadcasting | -0.0206 | ❌ |
| 31 | Southern California's economy can be described as ... | diverse | div diverse | 0.0000 | ❌ |
| 32 | In the definition based off the mountain range, wh... | southern | the southern | -0.2651 | ❌ |
| 33 | Where is Redland University located? | NO ANSWER | NO ANSWER | 0.4474 | ✅ |
| 34 | What is the integer practice problem? | NO ANSWER | NO ANSWER | 0.6589 | ✅ |
| 35 | What main business district is in downtown Los Ang... | NO ANSWER | The Downtown Los Angeles central business district | 0.0000 | ❌ |
| 36 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | 0.4187 | ✅ |
| 37 | What is the softest problem in C? | NO ANSWER | NO ANSWER | 0.6091 | ✅ |
| 38 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | All set top boxes in a household to share recordings and other media | 0.0000 | ❌ |
| 39 | A specific algorithm demonstrating T(n) represents... | upper bound | NO ANSWER | 0.0261 | ❌ |
| 40 | Complexity theory classifies problems based on wha... | difficulty | problems based on their difficulty | -0.0153 | ❌ |
| 41 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | -1.0000 | ✅ |
| 42 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | The Bakersfield-Kern County, Santa Maria and San Luis | 0.0000 | ❌ |
| 43 | What is the population of the second largest city ... | 1.3 million | The population of the 3 cities in southern California are 3 | -0.5186 | ❌ |
| 44 | Case complexities provide three likelihoods of wha... | inputs | NO ANSWER | 0.0288 | ❌ |
| 45 | What kind of universities is the region famous for... | research | research universities | -0.0961 | ❌ |
| 46 | What is a growing sport in southern California? | Rugby | Rugby | -0.8297 | ✅ |
| 47 | What is a typical type of computational problem wh... | NO ANSWER | Decision problem | -0.0544 | ❌ |
| 48 | What is an example of a measurement within a compl... | computation time | NO ANSWER | 0.0455 | ❌ |
| 49 | The legislation allowed California to be admitted ... | free | free state | 0.0000 | ❌ |

**correct binary classification:** 68.00% (34/50)

---

## new_main_trial_20260218_000133
**Timestamp:** 2026-02-18 00:01:37

**Dataset:** dev-data/official_50_sample-sample-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 54.46 |
| **NoAns Accuracy** | 34.78% (8/23) |
| **HasAns F1** | 71.22 |
| **HasAns EM** | 62.96 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |
| **Binary Classification** | 70.00% (35/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Margin | Status |
|-------|----------|---------------|------------------|--------|--------|
| 0 | What are two fields of theoretical computer scienc... | NO ANSWER | analysis of algorithms and computability theory | N/A | ❌ |
| 1 | What kind of universities is the region famous for... | research | public and private institutions | N/A | ❌ |
| 2 | What is the integer practice problem? | NO ANSWER | NO ANSWER | N/A | ✅ |
| 3 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 4 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County | N/A | ❌ |
| 5 | In the definition based off the mountain range, wh... | southern | southern | N/A | ✅ |
| 6 | What main business district is in downtown Los Ang... | NO ANSWER | Downtown Los Angeles central business district | N/A | ❌ |
| 7 | What are three examples of complexity classes asso... | BPP, ZPP and RP | BPP, ZPP, and RP. | N/A | ❌ |
| 8 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems. | N/A | ❌ |
| 9 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | share recordings and other media | N/A | ❌ |
| 10 | What is the expression used to identify any given ... | DTIME(f(n)) | DTIME(f(n)) | N/A | ✅ |
| 11 | Sky UK Limited is now known by what name? | NO ANSWER | British Sky Broadcasting or BSkyB | N/A | ❌ |
| 12 | What isn't required by customers to get Sky+ funct... | NO ANSWER | A monthly fee | N/A | ❌ |
| 13 | How many California University campuses are there? | NO ANSWER | There are 17 California University campuses. | N/A | ❌ |
| 14 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | N/A | ✅ |
| 15 | Where is Redland University located? | NO ANSWER | University of Redlands | N/A | ❌ |
| 16 | How many customaries does Norman customary law hav... | two | Two | N/A | ✅ |
| 17 | The legislation allowed California to be admitted ... | free | free state | N/A | ❌ |
| 18 | What is a growing sport in southern California? | Rugby | Rugby | N/A | ✅ |
| 19 | What culture's arrival in Scotland is know as the ... | Norman | Norman | N/A | ✅ |
| 20 | What is a typical type of computational problem wh... | NO ANSWER | A decision problem. | N/A | ❌ |
| 21 | What company owns ACB? | NO ANSWER | The Walt Disney Company | N/A | ❌ |
| 22 | What kind of university is the California Institut... | private | private | N/A | ✅ |
| 23 | Complexity theory classifies problems based on wha... | difficulty | problems based on their difficulty | N/A | ❌ |
| 24 | A complexity resource can also be described as wha... | computational resource | communication | N/A | ❌ |
| 25 | What year did Richards fleet avoid a storm? | NO ANSWER | April 1191 | N/A | ❌ |
| 26 | Southern California's distinctive regions are divi... | economically | politically | N/A | ❌ |
| 27 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | Sant'Eufemia | N/A | ❌ |
| 28 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 29 | Point Conception is an example of a landmark among... | northern | a landmark among the Tehachapi Mountains and the northern boundary | N/A | ❌ |
| 30 | Who was Richard's fiancee? | Berengaria | Berengaria | N/A | ✅ |
| 31 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | Anglo-Saxon | N/A | ❌ |
| 32 | What is the population of the second largest city ... | 1.3 million | 1.3 million | N/A | ✅ |
| 33 | What is an example of a measurement within a compl... | computation time | A time and space hierarchy theorem. | N/A | ❌ |
| 34 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 35 | Who was given the highlights of most of the matche... | BBC | The BBC | N/A | ❌ |
| 36 | What is the softest problem in C? | NO ANSWER | NO ANSWER | N/A | ✅ |
| 37 | A specific algorithm demonstrating T(n) represents... | upper bound | upper | N/A | ❌ |
| 38 | What thesis specifies that a trinomial relationshi... | NO ANSWER | Cobham-Edmonds thesis | N/A | ❌ |
| 39 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | N/A | ✅ |
| 40 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 41 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 42 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | N/A | ✅ |
| 43 | What are the other four important complexity class... | NO ANSWER | BPP, ZPP, RP, and NC. | N/A | ❌ |
| 44 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | N/A | ✅ |
| 45 | What company was formed by the merger of Sky Telev... | BSkyB | British Satellite Broadcasting | N/A | ❌ |
| 46 | Case complexities provide three likelihoods of wha... | inputs | time | N/A | ❌ |
| 47 | What is the metric they use to determine how busy ... | passenger volume | passenger volume | N/A | ✅ |
| 48 | Where did the Normans carve out a principality bef... | NO ANSWER | Antioch | N/A | ❌ |
| 49 | Southern California's economy can be described as ... | diverse | diverse | N/A | ✅ |

**correct binary classification:** 70.00% (35/50)

---

## new_main_trial_20260218_003836
**Timestamp:** 2026-02-18 00:38:41

**Dataset:** dev-data/official_50_sample-sample-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 36.00 |
| **Overall F1** | 41.06 |
| **NoAns Accuracy** | 30.43% (7/23) |
| **HasAns F1** | 50.11 |
| **HasAns EM** | 40.74 |
| **Total Questions** | 50 (HasAns: 27, NoAns: 23) |
| **Binary Classification** | 68.00% (34/50) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Margin | Status |
|-------|----------|---------------|------------------|--------|--------|
| 0 | Southern California's distinctive regions are divi... | economically | geographically | N/A | ❌ |
| 1 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 2 | Complexity theory classifies problems based on wha... | difficulty | time | N/A | ❌ |
| 3 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County. | N/A | ❌ |
| 4 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | N/A | ✅ |
| 5 | What is the expression used to identify any given ... | DTIME(f(n)) | DTIME(f(n)) | N/A | ✅ |
| 6 | What is the integer practice problem? | NO ANSWER | There is no mention of "integer practice problem" in the given context. The context is about the integer factorization problem | N/A | ❌ |
| 7 | What culture's arrival in Scotland is know as the ... | Norman | Norman culture. | N/A | ❌ |
| 8 | What company was formed by the merger of Sky Telev... | BSkyB | Sky | N/A | ❌ |
| 9 | What year did Richards fleet avoid a storm? | NO ANSWER | April 1191 | N/A | ❌ |
| 10 | What are two fields of theoretical computer scienc... | NO ANSWER | Analysis of algorithms and computability theory. | N/A | ❌ |
| 11 | What kind of universities is the region famous for... | research | The region, known as the Tech Coast, is famous for its numerous prestigious and world-renowned research universities. | N/A | ❌ |
| 12 | What isn't required by customers to get Sky+ funct... | NO ANSWER | A monthly fee. | N/A | ❌ |
| 13 | Who was given the highlights of most of the matche... | BBC | The BBC was given the highlights of most of the matches. | N/A | ❌ |
| 14 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | They can share recordings and other media. | N/A | ❌ |
| 15 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 16 | Where did the Normans carve out a principality bef... | NO ANSWER | Antioch | N/A | ❌ |
| 17 | Where is Redland University located? | NO ANSWER | University of Redlands | N/A | ❌ |
| 18 | What is the metric they use to determine how busy ... | passenger volume | The metric they use to determine how busy airports are is not explicitly stated in the provided context. However, based on the | N/A | ❌ |
| 19 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | N/A | ✅ |
| 20 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | Sant'Eufemia | N/A | ❌ |
| 21 | What thesis specifies that a trinomial relationshi... | NO ANSWER | Cobham-Edmonds thesis | N/A | ❌ |
| 22 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | N/A | ✅ |
| 23 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 24 | A complexity resource can also be described as wha... | computational resource | Circuit complexity. | N/A | ❌ |
| 25 | Southern California's economy can be described as ... | diverse | diverse | N/A | ✅ |
| 26 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 27 | How many California University campuses are there? | NO ANSWER | There are 17 California University campuses mentioned in the context: | N/A | ❌ |
| 28 | What are three examples of complexity classes asso... | BPP, ZPP and RP | The three examples of complexity classes associated with definitions established by probabilistic Turing machines are: | N/A | ❌ |
| 29 | What is the population of the second largest city ... | 1.3 million | The second largest city in California is San Diego, with a population of 1.3 million people. | N/A | ❌ |
| 30 | What is an example of a measurement within a compl... | computation time | A good example of a measurement within a complexity class that would create a bigger set of problems if the bounds were relaxed is | N/A | ❌ |
| 31 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | N/A | ✅ |
| 32 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems. | N/A | ❌ |
| 33 | How many customaries does Norman customary law hav... | two | Two. | N/A | ❌ |
| 34 | In the definition based off the mountain range, wh... | southern | The desert portions of north Los Angeles County would be included in the southern California region. | N/A | ❌ |
| 35 | Sky UK Limited is now known by what name? | NO ANSWER | Sky UK Limited is now known as Sky. | N/A | ❌ |
| 36 | Case complexities provide three likelihoods of wha... | inputs | Case complexities provide three likelihoods of the **time** of a solution differing variable that remains the same size. | N/A | ❌ |
| 37 | What is a growing sport in southern California? | Rugby | Rugby | N/A | ✅ |
| 38 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | Anglo-Saxon. | N/A | ❌ |
| 39 | The legislation allowed California to be admitted ... | free | free | N/A | ✅ |
| 40 | Point Conception is an example of a landmark among... | northern | Point Conception is an example of a landmark among the Tehachapi Mountains boundary of southern California. | N/A | ❌ |
| 41 | What is a typical type of computational problem wh... | NO ANSWER | A decision problem. | N/A | ❌ |
| 42 | What main business district is in downtown Los Ang... | NO ANSWER | Downtown Los Angeles central business district | N/A | ❌ |
| 43 | What are the other four important complexity class... | NO ANSWER | The other four important complexity classes are: | N/A | ❌ |
| 44 | What is the softest problem in C? | NO ANSWER | NO ANSWER | N/A | ✅ |
| 45 | What company owns ACB? | NO ANSWER | The Walt Disney Company | N/A | ❌ |
| 46 | What kind of university is the California Institut... | private | The California Institute of Technology is a private institution. | N/A | ❌ |
| 47 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | N/A | ✅ |
| 48 | Who was Richard's fiancee? | Berengaria | Berengaria | N/A | ✅ |
| 49 | A specific algorithm demonstrating T(n) represents... | upper bound | An upper bound. | N/A | ❌ |

**correct binary classification:** 68.00% (34/50)

---

