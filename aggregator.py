from typing import Dict, List


def aggregate_skill_frequency(results: List[Dict]) -> Dict[str, int]:
    """
    Aggregate skill frequency across analyzed job results.

    :param results: Output from the analysis pipeline
    :return: Dictionary mapping skill -> count
    """

    skill_counts: Dict[str, int] = {}

    for item in results:
        analysis = item.get("analysis", {})
        skills = analysis.get("skills", [])

        for skill in skills:
            # Increment count for each skill
            if skill in skill_counts:
                skill_counts[skill] += 1
            else:
                skill_counts[skill] = 1

    return skill_counts


def aggregate_seniority_distribution(results: List[Dict]) -> Dict[str, int]:
    """
    Aggregate seniority distribution across analyzed job results.

    :param results: Output from the analysis pipeline
    :return: Dictionary mapping seniority -> count
    """

    seniority_counts: Dict[str, int] = {
        "junior": 0,
        "mid": 0,
        "senior": 0,
        "unknown": 0,
    }

    for item in results:
        analysis = item.get("analysis", {})
        seniority = analysis.get("seniority", "unknown")

        # Defensive: count only known categories
        if seniority in seniority_counts:
            seniority_counts[seniority] += 1
        else:
            seniority_counts["unknown"] += 1

    return seniority_counts

def build_aggregation_summary(results: List[Dict]) -> Dict:
    """
    Build a combined aggregation summary from pipeline results.

    :param results: Output from the analysis pipeline
    :return: Dictionary containing all aggregation metrics
    """

    return {
        "skills": aggregate_skill_frequency(results),
        "seniority": aggregate_seniority_distribution(results),
    }
