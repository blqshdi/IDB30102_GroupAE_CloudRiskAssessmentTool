# Evaluation Plan & Test Scenarios

## 1. Overview
This document outlines the evaluation framework used to test the functionality and performance of the Cloud Risk Assessment Tool (CRAT) prototype. The evaluation compares CRAT's automated outputs against a manual $5 \times 5$ risk matrix baseline using synthetic cloud security risk scenarios.

---

## 2. Evaluation Metrics & Mathematical Formulas

| Metric | Description / Purpose | Formula |
| :--- | :--- | :--- |
| **Risk Score Correctness (%)** | Measures whether CRAT accurately calculates the mathematical risk score. | $\text{Risk Score Correctness (\%)} = \left( \frac{\text{Correct Risk Scores}}{\text{Total Test Cases}} \right) \times 100$ |
| **Classification Accuracy (%)** | Measures whether CRAT assigns the correct severity level (Low, Medium, High, Very High)[cite: 3]. | $\text{Classification Accuracy (\%)} = \left( \frac{\text{Correct Classifications}}{\text{Total Test Cases}} \right) \times 100$ |
| **Prioritization Agreement (%)** | Measures whether risks are ranked in the exact descending order of severity[cite: 3]. | $\text{Prioritization Agreement (\%)} = \left( \frac{\text{Correct Positions}}{\text{Total Positions}} \right) \times 100$] |
| **Processing Time (seconds)** | Measures the execution time taken by CRAT to process, classify, and sort scenarios[cite: 3]. | Recorded via `time.time()` execution timestamps in Python. |

---

## 3. Baseline & Boundary Classification Rules

### Manual $5 \times 5$ Risk Matrix Baseline
The manual baseline calculates risk scores using:
$$\text{Risk Score} = \text{Likelihood} \times \text{Impact} \quad (\text{where Likelihood}, \text{Impact} \in [1, 5])$$


### Severity Threshold Matrix
Boundary scores (such as 4/5, 9/10, and 16/17) are specifically evaluated to verify threshold boundary logic:

| Score Range | Severity Level | Target Threshold |
| :---: | :---: | :---: |
| **1 – 4** | Low | Boundary Upper: 4|
| **5 – 9** | Medium | Boundary Lower: 5, Upper: 9|
| **10 – 16** | High | Boundary Lower: 10, Upper: 16 |
| **17 – 25** | Very High | Boundary Lower: 17 |

---

## 4. Synthetic Evaluation Dataset (9 Core Test Scenarios)

The test cases represent common cloud security threat vectors compiled from reviewed literature themes:

| Test ID | Asset Name | Threat Vector | Vulnerability | Likelihood (1-5) | Impact (1-5) | Expected Score | Expected Level |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **TC-01** | Cloud Storage Bucket | Public Data Leakage | Misconfigured Permissions | 4 | 5 | 20 | Very High |
| **TC-02** | IAM Server | Credential Theft | Missing MFA Controls | 5 | 4 | 20 | Very High |
| **TC-03** | Kubernetes API | Remote Code Execution | Unpatched System OS | 4 | 4 | 16 | High |
| **TC-04** | API Gateway | Service Disruption | Missing Rate Limiting Rules | 3 | 3 | 9 | Medium |
| **TC-05** | Production Cloud DB | SQL Injection / Data Theft | Unsanitized Input Forms | 2 | 4 | 8 | Medium |
| **TC-06** | Compute Engine VM | Unauthorized Access | Weak Admin Passwords | 5 | 1 | 5 | Medium |
| **TC-07** | Backup Repository | Ransomware Encryption | Offline Backups Missing | 1 | 4 | 4 | Low |
| **TC-08** | Cloud DNS Service | Cache Poisoning | Lack of DNSSEC Validation | 2 | 2 | 4 | Low |
| **TC-09** | Staging Web Server | Information Disclosure | Default Configuration Active | 1 | 1 | 1 | Low |
