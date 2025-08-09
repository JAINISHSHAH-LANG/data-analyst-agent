# Data Analyst Agent

An AI-powered data analysis assistant that:
- Parses user prompts into a structured analysis plan
- Fetches data from sources like Wikipedia, CSVs, and S3 parquet files
- Performs analysis using DuckDB & Pandas
- Generates visualizations (Matplotlib)
- Returns results in a structured JSON or text array format

## Quickstart

1. Create virtualenv and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run app:

```bash
uvicorn app.main:app --reload --port 8000
```

3. Test sample prompt:

```bash
curl -X POST -F "file=@tests/prompts/01_wiki_rank_peak.txt" http://127.0.0.1:8000/
```
