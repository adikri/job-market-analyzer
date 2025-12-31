import csv
from typing import List
from models import Job

REQUIRED_FIELDS = {"job_id", "title", "company", "description", "source"}

def load_jobs_from_csv(file_path: str) -> List[Job]:
    jobs = []

    with open(file_path, newline="", encoding = "utf-8") as f:
        reader = csv.DictReader(f)

        if not REQUIRED_FIELDS.issubset(reader.fieldnames):
            missing = REQUIRED_FIELDS - set(reader.fieldnames)
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

