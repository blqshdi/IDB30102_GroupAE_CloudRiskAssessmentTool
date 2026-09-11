# Cloud Risk Assessment Tool (CRAT) - Source Code

## 1. Overview

This folder contains the preliminary source code for the **Cloud Risk Assessment Tool (CRAT)** developed for the research project:

**Assessing and Prioritizing Information Security Risks in Cloud Environments Using a Risk Assessment Tool**

The source code is implemented in **Python** and provides a simple command-line prototype for assessing, classifying and prioritizing information security risks in cloud environments.

The prototype is designed to demonstrate the technical feasibility of the proposed research solution.

---

## 2. Source Code

The main source code file is:

```text
main.py
```

The complete prototype functionality is combined into a single Python file.

```text
04_Source_Code/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 3. Programming Language

The prototype is developed using:

* **Python**
* Python Standard Library

The prototype uses the built-in `time` module to measure processing time.

No external Python libraries are required.

---

## 4. Main Components

The `main.py` program contains the following components:

### 4.1 Asset Options

The prototype provides predefined cloud assets:

```text
Cloud Database
Cloud Storage
Cloud Application
Cloud Backup
Cloud API
```

These represent examples of cloud resources that may be affected by information security risks.

---

### 4.2 Threat Options

The prototype provides predefined threats:

```text
Unauthorised Access
Data Exposure
Malware
Data Loss
Denial of Service
```

These threats represent common information security risks that may affect cloud environments.

---

### 4.3 Vulnerability Options

The prototype provides predefined vulnerabilities:

```text
Weak Authentication
Misconfigured Permissions
Unpatched Software
Excessive Privileges
Insufficient Backup
```

These vulnerabilities are used together with the selected asset and threat to describe a risk scenario.

---

## 5. Risk Assessment Process

The user can select:

1. Asset
2. Threat
3. Vulnerability
4. Likelihood
5. Impact

Likelihood and impact are rated from **1 to 5**.

The prototype calculates the risk score using:

```text
Risk Score = Likelihood × Impact
```

For example:

```text
Likelihood = 4
Impact = 5

Risk Score = 4 × 5
           = 20
```

The resulting score is then passed to the risk classification function.

---

## 6. Risk Classification

The `risk_level()` function classifies the calculated risk score.

| Risk Score | Risk Level |
| ---------: | ---------- |
|      1 - 4 | Low        |
|      5 - 9 | Medium     |
|    10 - 16 | High       |
|    17 - 25 | Very High  |

This allows the prototype to provide a consistent risk level based on the calculated score.

---

## 7. Risk Assessment Function

The `assess_risk()` function performs the main risk assessment process.

The function:

1. Allows the user to select an asset.
2. Allows the user to select a threat.
3. Allows the user to select a vulnerability.
4. Requests a likelihood rating.
5. Requests an impact rating.
6. Calculates the risk score.
7. Determines the risk level.
8. Displays the risk result.
9. Stores the assessed risk for later prioritization.

The result contains:

```text
Asset
Threat
Vulnerability
Likelihood
Impact
Risk Score
Risk Level
```

---

## 8. Risk Prioritisation

The `prioritise()` function is used when multiple risks have been assessed.

The prototype sorts risks according to their risk score:

```text
Highest Risk Score
        ↓
      Lower
        ↓
Lowest Risk Score
```

For example:

```text
Priority 1 | Cloud Database | Score: 20 | Very High
Priority 2 | Cloud API      | Score: 12 | High
Priority 3 | Cloud Storage  | Score: 8  | Medium
```

This allows higher-risk items to be identified first.

---

## 9. Prototype Evaluation

The `evaluate()` function provides preliminary evaluation of the prototype.

The evaluation contains four main areas:

1. Risk Score Correctness
2. Risk Classification Accuracy
3. Processing Time
4. Risk Prioritisation Agreement

---

### 9.1 Risk Score Correctness

The prototype uses predefined test cases containing:

```text
Likelihood
Impact
Expected Risk Score
Expected Risk Level
```

The calculated score is compared with the expected score.

The percentage is calculated using:

```text
Risk Score Correctness (%)
=
Correct Risk Scores / Total Test Cases × 100
```

---

### 9.2 Risk Classification Accuracy

The calculated risk level is compared with the expected risk level for each test case.

The percentage is calculated using:

```text
Classification Accuracy (%)
=
Correct Classifications / Total Test Cases × 100
```

The evaluation includes different risk levels:

```text
Low
Medium
High
Very High
```

---

### 9.3 Processing Time

The Python `time.perf_counter()` function is used to measure the processing time of the evaluation tests.

The program records:

```text
Start Time
    ↓
Run Evaluation
    ↓
End Time
    ↓
Calculate Processing Time
```

The result is displayed in seconds.

---

### 9.4 Risk Prioritisation Agreement

The prototype also evaluates whether the prioritization produced by CRAT agrees with the expected manual baseline ranking.

The expected ranking is:

```text
Cloud Database → Score 20
Cloud API      → Score 12
Cloud Storage  → Score 8
```

The test data is intentionally provided in a different order so that the prototype must sort the risks.

The prioritization agreement is calculated using:

```text
Prioritisation Agreement (%)
=
Correct Positions / Total Positions × 100
```

---

## 10. Main Menu

When `main.py` is executed, the user is presented with the following menu:

```text
================================
   CLOUD RISK ASSESSMENT TOOL
================================

1. Assess Risk
2. Prioritise Risks
3. Run Evaluation
4. Exit

================================
```

### Option 1 - Assess Risk

Allows the user to create a new risk assessment.

The user selects the asset, threat and vulnerability, then enters likelihood and impact values.

---

### Option 2 - Prioritise Risks

Displays all risks that have already been assessed and sorts them from the highest risk score to the lowest.

If no risk has been assessed, the system displays:

```text
No risks assessed yet.
```

---

### Option 3 - Run Evaluation

Runs the predefined evaluation tests for:

* Risk score correctness
* Risk classification accuracy
* Processing time
* Risk prioritisation agreement

---

### Option 4 - Exit

Closes the program and displays:

```text
Thank you!
```

---

## 11. Input Validation

The prototype includes input validation to prevent invalid values.

For menu selections, the user must choose a valid option.

For likelihood and impact:

```text
1 ≤ Rating ≤ 5
```

If the user enters a value outside the range, the program displays:

```text
Please enter a number from 1 to 5.
```

If the user enters non-numeric input, the program displays:

```text
Please enter a number.
```

This helps ensure that only valid risk-rating values are used in the calculation.

---

## 12. Example Risk Assessment

Example input:

```text
Asset:
Cloud Database

Threat:
Unauthorised Access

Vulnerability:
Weak Authentication

Likelihood:
5

Impact:
5
```

The prototype calculates:

```text
Risk Score = 5 × 5
           = 25
```

The risk is classified as:

```text
Risk Level: Very High
```

---

## 13. Example Prioritisation

If the user has three assessed risks:

```text
Cloud Storage  → Score 8
Cloud Database → Score 20
Cloud API      → Score 12
```

The prototype sorts them as:

```text
Priority 1 | Cloud Database | Score: 20 | Very High
Priority 2 | Cloud API      | Score: 12 | High
Priority 3 | Cloud Storage  | Score: 8  | Medium
```

This demonstrates the prioritization functionality of CRAT.

---

## 14. Example Evaluation Output

A typical evaluation output contains:

```text
1. RISK SCORE CORRECTNESS
100.0 %

2. RISK CLASSIFICATION ACCURACY
100.0 %

3. PROCESSING TIME
[measured value] seconds

4. RISK PRIORITISATION

Prioritisation Agreement:
100.0 %
```

The processing-time value depends on the computer and execution environment.

The percentages above are based on the predefined test cases in the prototype and should not be presented as final experimental research results.

---

## 15. How to Run

### Requirement

Python 3 is required.

Check the Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### Run the Prototype

Open Command Prompt or Terminal in this folder and run:

```bash
python main.py
```

The main menu will appear.

---

## 16. Running the Program

Example:

```text
================================
   CLOUD RISK ASSESSMENT TOOL
================================
1. Assess Risk
2. Prioritise Risks
3. Run Evaluation
4. Exit
================================
Choose:
```

Enter:

```text
1
```

to perform a risk assessment.

Enter:

```text
2
```

to prioritize the assessed risks.

Enter:

```text
3
```

to run the prototype evaluation.

Enter:

```text
4
```

to exit the program.

---

## 17. Technical Flow

The overall technical flow of `main.py` is:

```text
                    START
                      |
                      v
               Main Menu
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
     Assess Risk  Prioritise  Evaluation
          |           |           |
          v           v           v
     Select Asset   Sort Risks   Run Tests
          |           |           |
          v           v           v
     Select Threat  Highest     Calculate
          |         Score First  Accuracy
          v           |           |
   Select Vulnerability           v
          |                 Measure Time
          v                       |
     Enter Likelihood             v
          |                Check Prioritisation
          v                       |
       Enter Impact               v
          |                    Results
          v
   Calculate Risk Score
          |
          v
   Classify Risk Level
          |
          v
      Store Risk
          |
          v
        Result
```

---

## 18. Relationship to Research Objectives

The source code supports the research objectives as follows:

| Research Objective                                                                                                             | Source Code Contribution                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| RO1: Analyze existing information security risk assessment approaches used in cloud environments.                              | The predefined assets, threats, vulnerabilities and risk assessment approach represent the technical direction identified from the literature review. |
| RO2: Develop a prototype risk assessment tool for assessing and prioritizing information security risks in cloud environments. | `main.py` implements risk assessment, risk scoring, risk classification and risk prioritization.                                                      |
| RO3: Evaluate the functionality and risk prioritization performance of the proposed prototype tool.                            | The `evaluate()` function tests risk-score correctness, classification accuracy, processing time and prioritization agreement.                        |

---

## 19. Relationship to the Research Methodology

The source code represents the **Prototype Development** stage of the selected Design Science Research approach.

The technical development follows:

```text
Problem Identification
        ↓
Requirement and Design
        ↓
Prototype Development
        ↓
Demonstration and Evaluation
        ↓
Communication of Findings
```

The `main.py` prototype is therefore a preliminary technical component supporting the proposed research.

---

## 20. Relationship to the Manual Baseline

The evaluation section includes a manual-baseline comparison for prioritization.

The expected ranking is defined before the prototype sorts the test risks.

The comparison uses the same risk-score concept:

```text
Risk Score = Likelihood × Impact
```

This provides a simple reference for evaluating whether the prototype produces the expected prioritization order.

---

## 21. Limitations

The current source code is a preliminary academic prototype.

It does not provide:

* Real-time threat detection
* Penetration testing
* Machine learning
* Real cloud monitoring
* Real organizational risk data
* Enterprise risk management functionality
* Database storage
* Web-based interface

The prototype uses predefined options and synthetic test scenarios.

---

## 22. Academic Purpose

The purpose of this source code is to demonstrate the technical feasibility of the proposed **Cloud Risk Assessment Tool (CRAT)** at the research proposal stage.

The assignment states that a complete final system is not required at the proposal stage. Preliminary technical components can be provided to demonstrate the technical direction and feasibility of the proposed research.

---

## 23. Source Code File

The main implementation is available at:

```text
main.py
```

All major prototype functions are intentionally combined into this single file for simplicity:

```text
risk_level()
choose_option()
get_rating()
assess_risk()
prioritise()
evaluate()
```

The program is controlled through the main menu at the bottom of `main.py`.

---

## 24. External Code and Libraries

The prototype does not use third-party source code.

The only imported module is:

```python
import time
```

The `time` module is part of Python's standard library and is used to measure processing time during evaluation.

---

## 25. Summary

The `main.py` prototype demonstrates the core functionality of the proposed Cloud Risk Assessment Tool:

```text
Risk Input
    ↓
Risk Calculation
    ↓
Risk Classification
    ↓
Risk Storage
    ↓
Risk Prioritisation
    ↓
Prototype Evaluation
```

The source code provides the preliminary technical foundation for the proposed research and can be extended during future development and evaluation.
