from abc import ABC, abstractmethod
from typing import List

from models import Job


class JobSource(ABC):
    """
    Abstract base class for all job ingestion sources.
    """

    @abstractmethod
    def load_jobs(self) -> List[Job]:
        """
        Load jobs from a source and return a list of Job objects.
        """
        pass
