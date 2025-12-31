import requests
from typing import List

from models import Job
from ingestion.base import JobSource


class APIJobSource(JobSource):
    """
    JobSource implementation that loads jobs from the Remotive public API.
    """

    API_URL = "https://remotive.com/api/remote-jobs"

    def load_jobs(self) -> List[Job]:
        try:
            response = requests.get(self.API_URL, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            # Network errors, timeouts, non-200 responses
            raise RuntimeError("Failed to fetch jobs from API") from e

        data = response.json()

        if "jobs" not in data or not isinstance(data["jobs"], list):
            raise ValueError("Unexpected API response format")

        jobs: List[Job] = []

        for item in data["jobs"]:
            try:
                job = Job(
                    job_id=str(item.get("id")),
                    title=(item.get("title") or "").strip(),
                    company=(item.get("company_name") or "").strip(),
                    description=(item.get("description") or "").strip(),
                    source="api",
                )
                jobs.append(job)
            except Exception:
                # Skip malformed job entries instead of breaking ingestion
                continue

        return jobs
