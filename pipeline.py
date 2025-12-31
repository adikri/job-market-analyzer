from typing import List, Dict

from analyzer import analyze_job_description
from ingestion.base import JobSource
from models import Job


def analyze_jobs(source: JobSource) -> List[Dict]:
    """
    End-to-end pipeline:
    - Load jobs from a JobSource (CSV, API, etc.)
    - Analyze each job description using LLM
    - Attach structured results to each job
    """

    # Step 1: Load jobs from the provided source
    jobs: List[Job] = source.load_jobs()

    results: List[Dict] = []

    # Step 2: Iterate over each job
    for job in jobs:
        # Analyze job description using LLM
        analysis = analyze_job_description(job.description)

        # Combine metadata with analysis
        result = {
            "job_id": job.job_id,
            "title": job.title,
            "company": job.company,
            "analysis": analysis,
        }

        results.append(result)

    return results
