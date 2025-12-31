from typing import List, Dict

from ingestion import load_jobs_from_csv
from analyzer import analyze_job_description
from models import Job


def analyze_jobs(file_path: str) -> List[Dict]:
    """
    End-to-end pipeline:
    - Load jobs from CSV
    - Analyze each job description using LLM
    - Attach structured results to each job
    """

    # Step 1: Load Job objects from CSV
    jobs: List[Job] = load_jobs_from_csv(file_path)

    results = []

    # Step 2: Iterate over each job
    for job in jobs:
        # Call the LLM analyzer on the job description
        analysis = analyze_job_description(job.description)

        # Combine job metadata with LLM output
        result = {
            "job_id": job.job_id,
            "title": job.title,
            "company": job.company,
            "analysis": analysis,
        }

        results.append(result)

    return results
