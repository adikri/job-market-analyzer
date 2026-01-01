import streamlit as st

from ingestion.api_source import APIJobSource
from analyzer.factory import get_analyzer
from pipeline import analyze_jobs
from aggregator import build_aggregation_summary


st.set_page_config(page_title="Job Market Analyzer", layout="wide")

st.title("Job Market Analyzer")
st.caption("LLM-powered job insights (mock mode by default)")

# Show analyzer mode
analyzer = get_analyzer()
st.sidebar.header("Configuration")
st.sidebar.write(f"Analyzer in use: `{type(analyzer).__name__}`")

# Load data
with st.spinner("Analyzing jobs..."):
    source = APIJobSource()
    results = analyze_jobs(source, analyzer)
    summary = build_aggregation_summary(results)

st.success("Analysis complete")

# ---- Job List ----
st.header("Jobs")
for job in results[:10]:
    st.write(f"**{job['title']}** — {job['company']}")

# ---- Skill Frequency ----
st.header("Top Skills")
skill_data = summary["skills"]
st.bar_chart(skill_data)

# ---- Seniority Distribution ----
st.header("Seniority Distribution")
seniority_data = summary["seniority"]
st.bar_chart(seniority_data)
