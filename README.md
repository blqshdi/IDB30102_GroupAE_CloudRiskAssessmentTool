# Assessing and Prioritizing Information Security Risks in Cloud Environments Using a Risk Assessment Tool

## IDB30102 - Research Methodology

**Programme:** Bachelor in Computer System Security
**University:** Universiti Kuala Lumpur (UniKL)  
**Course:** IDB30102 - Research Methodology

## Research Title

**Assessing and Prioritizing Information Security Risks in Cloud Environments Using a Risk Assessment Tool**

## Group Members

1. ADAM BIN MOHAMAD ZAFERIZAM (52215125889)
2. NUR AZWA BINTI ABDUL KADIR (52215226132)
3. PUTRINURALISYA BINTI AB KADIR (52215226083)
4. NURUL BALQIS BINTI ABD HADI (52215125076)

## Research Aim

To develop a Cloud Risk Assessment Tool (CRAT) as a prototype for assessing and prioritizing information security risks in cloud environments. The prototype calculates risk scores, classifies risk levels and prioritizes identified risks. The results are evaluated against a manual 5×5 risk matrix baseline.

## Research Objectives

1. To analyze existing information security risk assessment approaches used in cloud environments.
2. To develop a prototype risk assessment tool for assessing and prioritizing information security risks in cloud environments.
3. To evaluate the functionality and risk prioritization performance of the proposed prototype tool.

## Proposed Solution

The **Cloud Risk Assessment Tool (CRAT)** is a simple Python prototype. It accepts asset, threat, vulnerability, likelihood and impact as inputs.

The risk score is:

```text
Risk Score = Likelihood × Impact
```

Risk levels:

| Score | Level |
|---:|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Very High |

Multiple risks can be prioritized from the highest score to the lowest score.

## Research Methodology

The research uses **Design Science Research (DSR)** with five phases:

1. Problem Identification
2. Requirement and Design
3. Prototype Development
4. Demonstration and Evaluation
5. Communication of Findings

The development model is the **Prototyping Model**.

## Dataset and Testing

The proposal uses findings from 43 reviewed papers to identify common cloud-security risk themes. Testing uses synthetic scenarios, including unauthorized access, data exposure, malware, data loss, denial of service, weak authentication and misconfigured permissions.

Likelihood and impact are controlled inputs from 1 to 5.

## Evaluation Plan

CRAT will be compared with a manual 5×5 risk matrix baseline.

Metrics:

- Risk Score Correctness
- Classification Accuracy
- Prioritization Agreement
- Processing Time

Boundary scores such as 4/5, 9/10 and 16/17 are tested to verify classification thresholds.

## Architecture

```text
User
  ↓
Risk Input
  ↓
Risk Calculation
  ↓
Risk Classification
  ↓
Risk Prioritization
  ↓
Risk Result
```

## Repository Structure

```text
IDB30102_GroupX_CloudRiskAssessmentTool/
├── README.md
├── 01_Research_Papers/
├── 02_Literature_Review/
├── 03_Architecture_and_Flowchart/
├── 04_Source_Code/
├── 05_Data_or_Sample_Input/
├── 06_Results_or_Expected_Output/
└── 07_References/
```

## Running the Preliminary Prototype

Open a terminal in `04_Source_Code/`.

Run:

```bash
python main.py
```

The prototype uses Python standard-library modules only.

## Scope

The research focuses on risk assessment and prioritization. Real-time attack detection, penetration testing and machine learning are outside the current scope.

## Ethical and Legal Considerations

Synthetic data is used. The project does not use personal, confidential or real organisational information, real credentials or unauthorized attacks.

## Repository Purpose

This repository provides evidence of the group's research activities and preliminary technical work. It connects the literature review to the proposed methodology, architecture, prototype and evaluation plan.

## Project Status

| Component | Status |
|---|---|
| Research Problem | Completed |
| Research Aim | Completed |
| Research Objectives | Completed |
| Literature Review | Completed |
| Research Gap | Completed |
| Research Methodology | Completed |
| Development Model | Completed |
| CRAT Architecture | Proposed |
| Preliminary Python Prototype | Included |
| Synthetic Test Data | Included |
| Manual Baseline | Included |
| Evaluation Plan | Included |
| Final Experimental Results | Included |

## Disclaimer

CRAT is an academic research prototype. It is not intended to replace professional information-security risk assessment, enterprise risk management, security audits or penetration testing.
