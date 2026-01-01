import os

from analyzer.base import Analyzer
from analyzer.llm_analyzer import LLMAnalyzer
from analyzer.mock_analyzer import MockAnalyzer


def get_analyzer() -> Analyzer:
    """
    Factory function to select the appropriate Analyzer implementation.

    Controlled by environment variable:
    USE_REAL_LLM=true | false
    """

    use_real_llm = os.getenv("USE_REAL_LLM", "false").lower()

    if use_real_llm == "true":
        return LLMAnalyzer()

    return MockAnalyzer()
