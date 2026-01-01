# Job Market Analyzer — LLM-Powered Job Intelligence System

**Live Demo:**  
https://job-market-analyzer-yborm8cj2smfruf3zcek8a.streamlit.app

---

## 1. Problem Statement

Job descriptions are unstructured, inconsistent, and difficult to analyze at scale.  
Recruiters, job seekers, and hiring teams lack aggregated insights such as:

- Which skills are most in demand?
- What seniority levels dominate the market?
- How trends differ across job postings?

Manual analysis does not scale.

---

## 2. Solution Overview

This project is an end-to-end job intelligence system that:

- Ingests job postings from public APIs
- Uses a Large Language Model (LLM) to extract structured insights
- Aggregates results across postings
- Visualizes insights through an interactive web UI

The system is designed with production concerns in mind, including:

- Cost control
- Fault isolation
- Deterministic testing
- Safe defaults

---

## 3. Live Demo

The application is publicly deployed using Streamlit Cloud:

https://job-market-analyzer-yborm8cj2smfruf3zcek8a.streamlit.app

### Demo Features

- Job listing view
- Skill frequency visualization
- Seniority distribution analysis
- UI toggle between:
  - Mock analyzer (safe, zero cost)
  - Real LLM analyzer (explicit opt-in)

---

## 4. Architecture Overview

Ingestion Layer
├── CSV source
└── API source (Remotive)

Pipeline Layer
└── Orchestrates ingestion → analysis → aggregation

Analyzer Layer
├── MockAnalyzer (deterministic, test-safe)
└── LLMAnalyzer (OpenAI-powered, cached)

Aggregation Layer
├── Skill frequency
└── Seniority distribution

Presentation Layer
└── Streamlit UI

---

## 5. Key Design Decisions

### Analyzer Abstraction (Dependency Inversion)

- The pipeline depends on an Analyzer interface, not a concrete LLM
- Enables mock testing, cost-free development, and easy model replacement

---

### Cost Control by Design

- LLM usage is disabled by default
- Real LLM calls require explicit UI opt-in
- Prevents accidental spend

---

### LLM Response Caching

- LLM outputs are cached using a content-based hash
- Identical job descriptions reuse previous results
- Reduces latency and API cost

---

### Robust JSON Parsing

- Handles markdown-wrapped LLM responses
- Fails fast on malformed outputs
- Prevents downstream pipeline failures

---

### Separation of Concerns

Each layer has a single responsibility:

- Ingestion ≠ Analysis ≠ Aggregation ≠ UI

This makes the system testable, maintainable, and scalable.

---

## 6. Technology Stack

- Language: Python
- LLM: OpenAI (GPT-4o-mini)
- UI: Streamlit
- Data Sources: Public job APIs
- Architecture: Modular, interface-driven
- Deployment: Streamlit Cloud

---

## 7. Running Locally

```bash
git clone https://github.com/adikri/job-market-analyzer.git
cd job-market-analyzer
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Optional: Enable Real LLM

```bash
export OPENAI_API_KEY=your_key_here
```

Then toggle **“Use real LLM”** in the UI.

---

## 8. What This Project Demonstrates

- Applied GenAI system design
- Safe and testable LLM integration
- Production-aware engineering
- End-to-end ownership (API → LLM → UI → deployment)

---

## 9. Future Enhancements

- Skill normalization and taxonomy
- Time-based trend analysis
- Multi-source ingestion
- Role- or location-specific insights

---

## 10. Author

**Aditya Krishna**  
Applied GenAI / Backend Engineer
