# SQuAD 2.0 Trials Log

This file tracks all trial runs to monitor improvements and avoid over-correction.

---

## Exp_P0.01_B10_20260214_223154
**Timestamp:** 2026-02-14 22:37:13

**Parameters:** prob_threshold=0.01, bias_value=10.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 58.33 |
| **Overall F1** | 64.61 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 84.42 |
| **HasAns EM** | 75.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | quicksort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be stated that a problem set that is hard for the class NP is the | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.01_B15_20260214_223715
**Timestamp:** 2026-02-14 22:42:11

**Parameters:** prob_threshold=0.01, bias_value=15.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 33.33 |
| **Overall F1** | 53.81 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 68.21 |
| **HasAns EM** | 37.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sat satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | T Tehachapi Mountains | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.01_B20_20260214_224214
**Timestamp:** 2026-02-14 22:47:05

**Parameters:** prob_threshold=0.01, bias_value=20.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 33.33 |
| **Overall F1** | 51.59 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 64.88 |
| **HasAns EM** | 37.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | They receive their own satellite feeds. | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | T Tehachapi Mountains | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.01_B25_20260214_224707
**Timestamp:** 2026-02-14 22:52:07

**Parameters:** prob_threshold=0.01, bias_value=25.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 53.25 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 67.38 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sat satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | A monthly subscription. | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.01_B30_20260214_225209
**Timestamp:** 2026-02-14 22:57:15

**Parameters:** prob_threshold=0.01, bias_value=30.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 53.52 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 67.78 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | A relation | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | sat satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.05_B10_20260214_225718
**Timestamp:** 2026-02-14 23:02:32

**Parameters:** prob_threshold=0.05, bias_value=10.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 58.33 |
| **Overall F1** | 65.72 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 86.09 |
| **HasAns EM** | 75.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | The set of triples (a, b, c) such that the relation a × b = c holds. | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | quicksort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sky Q Mini set top boxes | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be stated that a problem set that is hard for the class NP is the | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | A monthly subscription. | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.05_B15_20260214_230234
**Timestamp:** 2026-02-14 23:07:50

**Parameters:** prob_threshold=0.05, bias_value=15.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 25.00 |
| **Overall F1** | 44.44 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 54.17 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | The set of triples (a, b, c) such that the relation a × b = c holds. | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sky Q Mini set top boxes | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | The size of the input is usually taken to be the size of the input in bits. | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | A monthly subscription. | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | T Tehachapi Mountains | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.05_B20_20260214_230751
**Timestamp:** 2026-02-14 23:12:58

**Parameters:** prob_threshold=0.05, bias_value=20.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 25.00 |
| **Overall F1** | 48.04 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 59.56 |
| **HasAns EM** | 25.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | A relation | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sat satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | The size of the input is usually taken to be the size of the input in bits. | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | T Tehachapi Mountains | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.05_B25_20260214_231300
**Timestamp:** 2026-02-14 23:17:59

**Parameters:** prob_threshold=0.05, bias_value=25.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 53.52 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 67.78 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sat satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.05_B30_20260214_231801
**Timestamp:** 2026-02-14 23:22:51

**Parameters:** prob_threshold=0.05, bias_value=30.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 33.33 |
| **Overall F1** | 51.85 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 65.28 |
| **HasAns EM** | 37.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sat satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | T Tehachapi Mountains | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.1_B10_20260214_232253
**Timestamp:** 2026-02-14 23:27:43

**Parameters:** prob_threshold=0.1, bias_value=10.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 56.28 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 71.92 |
| **HasAns EM** | 62.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | quicksort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be stated that a problem set that is hard for the class NP is the | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | A monthly subscription. | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | National | ❌ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.1_B15_20260214_232745
**Timestamp:** 2026-02-14 23:32:33

**Parameters:** prob_threshold=0.1, bias_value=15.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 56.85 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 72.78 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Other satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---## Exp_P0.1_B20_20260214_233235
**Timestamp:** 2026-02-14 23:37:29

**Parameters:** prob_threshold=0.1, bias_value=20.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 56.59 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 72.38 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sat satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | A monthly subscription. | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.1_B25_20260214_233730
**Timestamp:** 2026-02-14 23:42:22

**Parameters:** prob_threshold=0.1, bias_value=25.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 56.59 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 72.38 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | A relation | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Their own satellite feeds. | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.1_B30_20260214_234224
**Timestamp:** 2026-02-14 23:47:12

**Parameters:** prob_threshold=0.1, bias_value=30.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 33.33 |
| **Overall F1** | 51.59 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 64.88 |
| **HasAns EM** | 37.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sky Q Mini set top boxes | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be used to be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | T Tehachapi Mountains | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.5_B10_20260214_234713
**Timestamp:** 2026-02-14 23:52:09

**Parameters:** prob_threshold=0.5, bias_value=10.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 50.00 |
| **Overall F1** | 58.58 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 75.37 |
| **HasAns EM** | 62.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | quicksort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | They receive their own satellite feeds. | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be stated that a problem set that is hard for the class NP is the | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | The size of the input is usually taken to be the size of the input in bits. | ❌ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | ✅ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.5_B15_20260214_235211
**Timestamp:** 2026-02-14 23:57:04

**Parameters:** prob_threshold=0.5, bias_value=15.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 56.85 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 72.78 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | The set of triples (a, b, c) such that the relation a × b = c holds. | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sky Q Mini set top boxes | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.5_B20_20260214_235706
**Timestamp:** 2026-02-15 00:01:54

**Parameters:** prob_threshold=0.5, bias_value=20.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 33.33 |
| **Overall F1** | 48.75 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 60.62 |
| **HasAns EM** | 37.50 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | They receive their own satellite feeds. | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 1, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | National | ❌ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.5_B25_20260215_000156
**Timestamp:** 2026-02-15 00:06:43

**Parameters:** prob_threshold=0.5, bias_value=25.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 53.52 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 67.78 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Sat satellite feeds | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | a monthly subscription | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | YES, 0 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

## Exp_P0.5_B30_20260215_000645
**Timestamp:** 2026-02-15 00:11:33

**Parameters:** prob_threshold=0.5, bias_value=30.0

**Dataset:** dev-data/tiny_dev_12-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 41.67 |
| **Overall F1** | 55.74 |
| **NoAns Accuracy** | 25.00% (1/4) |
| **HasAns F1** | 71.11 |
| **HasAns EM** | 50.00 |
| **Total Questions** | 12 (HasAns: 8, NoAns: 4) |
| **Binary Classification** | 75.00% (9/12) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Status |
|-------|----------|---------------|------------------|--------|
| 0 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | ✅ |
| 1 | What is the expression set called where three inte... | NO ANSWER | Set of triples | ❌ |
| 2 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | qusort | ❌ |
| 3 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Their own satellite feeds. | ❌ |
| 4 | A problem set that that is hard for the expression... | NP-hard | The set of problems that are hard for NP can be commonly be the set of NP-hard problems. | ❌ |
| 5 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | ✅ |
| 6 | In what unit is the size of the input measured? | bits | bits | ✅ |
| 7 | What do encrypted broadcasts never require? | NO ANSWER | A monthly subscription. | ❌ |
| 8 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1 | ❌ |
| 9 | The Los Angeles Rams are an example of what kind o... | NFL | NFL | ✅ |
| 10 | What is the name of the desert near the border of ... | Mojave Desert | M Mojave Desert | ❌ |
| 11 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains. | ❌ |

**correct binary classification:** 75.00% (9/12)

---

