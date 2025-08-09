from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Define data models
class Plan(BaseModel):
    steps: List[str]

class Response(BaseModel):
    message: str
    plan: Optional[Plan] = None

# Initialize FastAPI app
app = FastAPI(
    title="Data Analyst Agent",
    description="An API that plans and executes data analysis tasks",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Data Analyst Agent API is running!"}

@app.post("/plan", response_model=Response)
def generate_plan(task: str):
    steps = [
        f"Understand the task: {task}",
        "Collect relevant data",
        "Clean and preprocess the data",
        "Analyze the data",
        "Visualize results",
        "Summarize and return insights"
    ]
    return Response(message="Plan generated successfully", plan=Plan(steps=steps))
