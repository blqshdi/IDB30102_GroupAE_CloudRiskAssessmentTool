# Evaluation Plan

## Baseline

Manual 5×5 risk matrix using:

**Risk Score = Likelihood × Impact**

## Test Inputs

Synthetic cloud-security risk scenarios with likelihood and impact values from 1 to 5.

## Metrics

### Risk Score Correctness

Correct Risk Scores / Total Test Cases × 100

### Classification Accuracy

Correct Classifications / Total Test Cases × 100

### Prioritization Agreement

Correct Positions / Total Positions × 100

### Processing Time

Measure the execution time required by the prototype.

## Boundary Testing

The classification boundaries include:

- 4 / 5
- 9 / 10
- 16 / 17

These pairs test the transitions between Low/Medium, Medium/High and High/Very High.

## Expected Comparison

For every scenario:

1. Calculate the expected manual score.
2. Calculate the expected manual risk level.
3. Run CRAT.
4. Compare the CRAT score with the baseline.
5. Compare the CRAT classification with the baseline.
6. Compare the prioritization order.
7. Record processing time.

Final percentages should only be filled after actual testing.
