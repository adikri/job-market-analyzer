from abc import ABC, abstractmethod
from typing import Dict, List


class Analyzer(ABC):
    """
    Contract for job description analyzers.
    """

    @abstractmethod
    def analyze(self, description: str) -> Dict[str, List[str] | str]:
        """
        Analyze a job description and return structured data.
        """
        pass
