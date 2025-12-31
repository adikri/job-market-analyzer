from typing import Dict, List

def analyze_job_description(description: str) -> Dict[str, List[str] | str]:
    """
    Analyze a job description and extract structured information.

    For now, this is a MOCK implementation.
    Later, we will replace this logic with a real LLM call.

    :param description: Raw job description text
    :return: Dictionary with extracted fields
    """
    # Defensive check: description must be non-empty
    if not description or not description.strip():
        raise ValueError("Job description is empty")
    
    # This is a mocked, deterministic response.
    # We are simulating what an LLM would return as JSON.

    result = {
        "skills": ["python"],
        "seniority": "unknown"
    }

    return result