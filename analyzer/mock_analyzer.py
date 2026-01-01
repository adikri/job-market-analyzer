from typing import Dict, List

from analyzer.base import Analyzer


class MockAnalyzer(Analyzer):
    """
    Fake analyzer for testing and development.

    This implementation:
    - Does NOT call any external APIs
    - Returns deterministic, hardcoded results
    - Obeys the same output contract as LLMAnalyzer
    """

    def analyze(self, description: str) -> Dict[str, List[str] | str]:
        """
        Return predictable analysis output regardless of input.
        """

        # We intentionally ignore the description
        # because this is a mock used for testing logic,
        # not for validating LLM behavior.
        return {
            "skills": ["python", "api"],
            "seniority": "mid",
        }
