from dataclasses import dataclass
from typing import Optional

@dataclass
class Job:
    job_id: str
    title: str
    company: str
    description: str
    source: str

