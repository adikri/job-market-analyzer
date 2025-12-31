import csv
from typing import List

from models import Job
from ingestion.base import JobSource


class CSVJobSource(JobSource):
    """
    JobSource implementation that loads jobs from a CSV file.
    """

    REQUIRED_FIELDS = {"job_id", "title", "company", "description", "source"}

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_jobs(self) -> List[Job]:
        jobs: List[Job] = []

        with open(self.file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if not self.REQUIRED_FIELDS.issubset(reader.fieldnames):
                missing = self.REQUIRED_FIELDS - set(reader.fieldnames)
                raise ValueError(f"Missing required fields: {missing}")

            for row in reader:
                job = Job(
                    job_id=row["job_id"].strip(),
                    title=row["title"].strip(),
                    company=row["company"].strip(),
                    description=row["description"].strip(),
                    source=row["source"].strip(),
                )
                jobs.append(job)

        return jobs
