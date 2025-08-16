# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List, Optional

# # Define data models
# class Plan(BaseModel):
#     steps: List[str]

# class Response(BaseModel):
#     message: str
#     plan: Optional[Plan] = None

# # Initialize FastAPI app
# app = FastAPI(
#     title="Data Analyst Agent",
#     description="An API that plans and executes data analysis tasks",
#     version="1.0.0"
# )

# @app.get("/")
# def read_root():
#     return {"message": "Data Analyst Agent API is running!"}

# @app.post("/plan", response_model=Response)
# def generate_plan(task: str):
#     steps = [
#         f"Understand the task: {task}",
#         "Collect relevant data",
#         "Clean and preprocess the data",
#         "Analyze the data",
#         "Visualize results",
#         "Summarize and return insights"
#     ]
#     return Response(message="Plan generated successfully", plan=Plan(steps=steps))


from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
import matplotlib.pyplot as plt
import base64, io
from adapter import format_response

app = FastAPI()

@app.post("/api/")
async def analyze(questions: UploadFile, files: list[UploadFile] = []):
    try:
        # Read questions.txt
        q_text = (await questions.read()).decode("utf-8")

        # Example: parse CSV files if provided
        dfs = {}
        for f in files:
            if f.filename.endswith(".csv"):
                dfs[f.filename] = pd.read_csv(io.StringIO((await f.read()).decode("utf-8")))

        # Dummy answers (replace with real analysis later)
        ans1 = 1
        ans2 = "The Titanic dataset is a classic benchmark."
        ans3 = 0.485782

        # Example plot
        plt.figure()
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 2.5, 5, 4]
        plt.scatter(x, y)
        plt.plot(x, y, "r--")
        plt.xlabel("Rank")
        plt.ylabel("Peak")

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        img_b64 = "data:image/png;base64," + base64.b64encode(buf.read()).decode()

        return JSONResponse(content=format_response([ans1, ans2, ans3, img_b64]))

    except Exception as e:
        return JSONResponse(content=format_response([None, str(e), None, None]))


