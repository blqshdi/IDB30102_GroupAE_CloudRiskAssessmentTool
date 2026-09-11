"""Cloud Risk Assessment Tool (CRAT) - preliminary academic prototype."""

from dataclasses import dataclass
from time import perf_counter


@dataclass
class Risk:
    asset: str
    threat: str
    vulnerability: str
    likelihood: int
    impact: int


def validate_rating(value: int) -> None:
    if not isinstance(value, int) or not 1 <= value <= 5:
        raise ValueError("Likelihood and impact must be integers from 1 to 5.")


def calculate_score(likelihood: int, impact: int) -> int:
    validate_rating(likelihood)
    validate_rating(impact)
    return likelihood * impact


def classify_risk(score: int) -> str:
    if not 1 <= score <= 25:
        raise ValueError("Risk score must be between 1 and 25.")
    if score <= 4:
        return "Low"
    if score <= 9:
        return "Medium"
    if score <= 16:
        return "High"
    return "Very High"


def assess_risk(risk: Risk) -> dict:
    score = calculate_score(risk.likelihood, risk.impact)
    return {
        "asset": risk.asset,
        "threat": risk.threat,
        "vulnerability": risk.vulnerability,
        "likelihood": risk.likelihood,
        "impact": risk.impact,
        "risk_score": score,
        "risk_level": classify_risk(score),
    }


def prioritize(risks: list[Risk]) -> list[dict]:
    assessed = [assess_risk(r) for r in risks]
    assessed.sort(key=lambda item: item["risk_score"], reverse=True)
    for position, item in enumerate(assessed, start=1):
        item["priority"] = position
    return assessed


def demo() -> None:
    scenarios = [
        Risk("Cloud database", "Unauthorized access", "Weak authentication", 5, 5),
        Risk("Object storage", "Data exposure", "Misconfigured permissions", 4, 5),
        Risk("Application server", "Malware", "Unpatched software", 3, 4),
    ]

    start = perf_counter()
    results = prioritize(scenarios)
    elapsed = perf_counter() - start

    print("\nCloud Risk Assessment Tool (CRAT)")
    print("=" * 55)
    for item in results:
        print(
            f'Priority {item["priority"]}: {item["asset"]} | '
            f'Score={item["risk_score"]} | Level={item["risk_level"]}'
        )
    print(f"Processing time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    demo()
