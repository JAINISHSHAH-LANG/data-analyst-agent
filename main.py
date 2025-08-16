# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from typing import List, Optional

# # # Define data models
# # class Plan(BaseModel):
# #     steps: List[str]

# # class Response(BaseModel):
# #     message: str
# #     plan: Optional[Plan] = None

# # # Initialize FastAPI app
# # app = FastAPI(
# #     title="Data Analyst Agent",
# #     description="An API that plans and executes data analysis tasks",
# #     version="1.0.0"
# # )

# # @app.get("/")
# # def read_root():
# #     return {"message": "Data Analyst Agent API is running!"}

# # @app.post("/plan", response_model=Response)
# # def generate_plan(task: str):
# #     steps = [
# #         f"Understand the task: {task}",
# #         "Collect relevant data",
# #         "Clean and preprocess the data",
# #         "Analyze the data",
# #         "Visualize results",
# #         "Summarize and return insights"
# #     ]
# #     return Response(message="Plan generated successfully", plan=Plan(steps=steps))


# from fastapi import FastAPI, UploadFile
# from fastapi.responses import JSONResponse
# import pandas as pd
# import matplotlib.pyplot as plt
# import base64, io
# from adapter import format_response

# app = FastAPI()

# @app.post("/api/")
# async def analyze(questions: UploadFile, files: list[UploadFile] = []):
#     try:
#         # Read questions.txt
#         q_text = (await questions.read()).decode("utf-8")

#         # Example: parse CSV files if provided
#         dfs = {}
#         for f in files:
#             if f.filename.endswith(".csv"):
#                 dfs[f.filename] = pd.read_csv(io.StringIO((await f.read()).decode("utf-8")))

#         # Dummy answers (replace with real analysis later)
#         ans1 = 1
#         ans2 = "The Titanic dataset is a classic benchmark."
#         ans3 = 0.485782

#         # Example plot
#         plt.figure()
#         x = [1, 2, 3, 4, 5]
#         y = [2, 3, 2.5, 5, 4]
#         plt.scatter(x, y)
#         plt.plot(x, y, "r--")
#         plt.xlabel("Rank")
#         plt.ylabel("Peak")

#         buf = io.BytesIO()
#         plt.savefig(buf, format="png")
#         buf.seek(0)
#         img_b64 = "data:image/png;base64," + base64.b64encode(buf.read()).decode()

#         return JSONResponse(content=format_response([ans1, ans2, ans3, img_b64]))

#     except Exception as e:
#         return JSONResponse(content=format_response([None, str(e), None, None]))


from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
import matplotlib.pyplot as plt
import base64, io, logging
import numpy as np
from adapter import format_response

# Setup logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Data Analyst Agent",
    description="API that analyzes uploaded datasets and answers questions",
    version="1.0.0"
)

@app.post("/api/")
async def analyze(questions: UploadFile, files: list[UploadFile] = []):
    try:
        # ✅ Read questions.txt
        q_text = (await questions.read()).decode("utf-8")
        logging.info(f"Questions received:\n{q_text}")

        # ✅ Load datasets
        dfs = {}
        for f in files:
            content = await f.read()
            if f.filename.endswith(".csv"):
                dfs[f.filename] = pd.read_csv(io.StringIO(content.decode("utf-8")))
            elif f.filename.endswith(".json"):
                dfs[f.filename] = pd.read_json(io.StringIO(content.decode("utf-8")))
            elif f.filename.endswith(".parquet"):
                dfs[f.filename] = pd.read_parquet(io.BytesIO(content))
            else:
                logging.warning(f"Unsupported file format: {f.filename}")

        if not dfs:
            return JSONResponse(content=format_response([None, "No valid dataset uploaded", None, None]))

        # For now, just use the first dataset
        df = list(dfs.values())[0]

        # ✅ Example Q1: Case count
        ans1 = len(df)

        # ✅ Example Q2: Summary string
        ans2 = f"Dataset {list(dfs.keys())[0]} has {df.shape[0]} rows and {df.shape[1]} columns."

        # ✅ Example Q3: Regression slope (dummy example with first 2 numeric cols)
        num_cols = df.select_dtypes(include=[np.number]).columns
        ans3 = None
        if len(num_cols) >= 2:
            x, y = df[num_cols[0]], df[num_cols[1]]
            slope, _ = np.polyfit(x.dropna(), y.dropna(), 1)
            ans3 = float(slope)
        else:
            ans2 += " (No numeric columns found for regression.)"

        # ✅ Example Q4: Scatter + regression plot
        img_b64 = None
        if len(num_cols) >= 2:
            plt.figure(figsize=(5, 4))
            plt.scatter(x, y, alpha=0.5)
            m, b = np.polyfit(x.dropna(), y.dropna(), 1)
            plt.plot(x, m*x+b, color="red", linestyle="--")
            plt.xlabel(num_cols[0])
            plt.ylabel(num_cols[1])
            plt.title("Scatter with regression line")

            buf = io.BytesIO()
            plt.savefig(buf, format="webp", dpi=80, bbox_inches="tight")
            buf.seek(0)
            img_b64 = "data:image/webp;base64," + base64.b64encode(buf.read()).decode()
            plt.close()

        return JSONResponse(content=format_response([ans1, ans2, ans3, img_b64]))

    except Exception as e:
        logging.exception("Error during analysis")
        return JSONResponse(content=format_response([None, str(e), None, None]))

