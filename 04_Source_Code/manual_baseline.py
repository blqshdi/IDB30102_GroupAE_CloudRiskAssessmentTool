"""Manual 5x5 baseline implementation for CRAT comparison."""

def manual_score(likelihood: int, impact: int) -> int:
    return likelihood * impact


def manual_classification(score: int) -> str:
    if 1 <= score <= 4:
        return "Low"
    if 5 <= score <= 9:
        return "Medium"
    if 10 <= score <= 16:
        return "High"
    if 17 <= score <= 25:
        return "Very High"
    raise ValueError("Score must be between 1 and 25.")


def baseline_result(likelihood: int, impact: int) -> tuple[int, str]:
    score = manual_score(likelihood, impact)
    return score, manual_classification(score)


if __name__ == "__main__":
    print("Manual 5x5 Risk Matrix Baseline")
    print("=" * 35)
    for likelihood, impact in [(1, 1), (2, 3), (3, 3), (4, 4), (5, 5)]:
        score, level = baseline_result(likelihood, impact)
        print(f"Likelihood={likelihood}, Impact={impact} -> {score} ({level})")
