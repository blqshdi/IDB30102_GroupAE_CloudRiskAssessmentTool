# CRAT System Architecture

## Main Architecture

```text
+----------------+
|      User      |
+-------+--------+
        |
        v
+----------------+
|   Risk Input   |
| Asset          |
| Threat         |
| Vulnerability  |
| Likelihood     |
| Impact         |
+-------+--------+
        |
        v
+----------------------+
|   Risk Calculation   |
| Score = L x I        |
+----------+-----------+
           |
           v
+----------------------+
| Risk Classification  |
| Low / Medium / High  |
| / Very High          |
+----------+-----------+
           |
           v
+----------------------+
| Risk Prioritization  |
| Highest -> Lowest    |
+----------+-----------+
           |
           v
+----------------+
|  Risk Result   |
+----------------+
```

## Input

- Asset
- Threat
- Vulnerability
- Likelihood: 1–5
- Impact: 1–5

## Processing

1. Validate likelihood and impact.
2. Calculate the risk score.
3. Classify the score.
4. Sort multiple risks by score.

## Output

The output contains the risk information, calculated score, risk level and priority position.
