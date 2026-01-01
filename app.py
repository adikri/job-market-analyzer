from ingestion.api_source import APIJobSource
from analyzer.factory import get_analyzer
from pipeline import analyze_jobs
from aggregator import build_aggregation_summary


def main():
    source = APIJobSource()
    analyzer = get_analyzer()
    print("Using analyzer:", type(analyzer))
    results = analyze_jobs(source, analyzer)
    summary = build_aggregation_summary(results)

    print("Sample job:")
    print(results[0])
    print("\nSummary:")
    print(summary)


if __name__ == "__main__":
    main()
