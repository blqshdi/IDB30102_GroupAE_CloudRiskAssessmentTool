import unittest
from crat import Risk, calculate_score, classify_risk, assess_risk, prioritize


class TestCRAT(unittest.TestCase):

    def test_score_calculation(self):
        self.assertEqual(calculate_score(3, 4), 12)

    def test_low_boundary(self):
        self.assertEqual(classify_risk(4), "Low")

    def test_medium_boundary(self):
        self.assertEqual(classify_risk(5), "Medium")

    def test_high_boundary(self):
        self.assertEqual(classify_risk(10), "High")

    def test_very_high_boundary(self):
        self.assertEqual(classify_risk(17), "Very High")

    def test_assessment(self):
        risk = Risk("Database", "Data exposure", "Misconfiguration", 4, 5)
        result = assess_risk(risk)
        self.assertEqual(result["risk_score"], 20)
        self.assertEqual(result["risk_level"], "Very High")

    def test_prioritization(self):
        risks = [
            Risk("A", "Threat A", "Vuln A", 2, 2),
            Risk("B", "Threat B", "Vuln B", 5, 5),
            Risk("C", "Threat C", "Vuln C", 3, 4),
        ]
        results = prioritize(risks)
        self.assertEqual(results[0]["asset"], "B")
        self.assertEqual(results[0]["priority"], 1)
        self.assertEqual(results[-1]["asset"], "A")


if __name__ == "__main__":
    unittest.main()
