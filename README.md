# Data Analyst Agent

A FastAPI-based agent that takes `questions.txt` + optional data files,  
runs analysis, and always returns a **4-element JSON array**.

## 🚀 Setup

```bash
git clone https://github.com/JAINISHSHAH-LANG/data-analyst-agent.git
cd data-analyst-agent
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
