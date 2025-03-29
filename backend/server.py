import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.question_agent import generate_questions
from agents.data_agent import gather_data
from agents.analysis_agent import analyze_data
from agents.report_agent import generate_pdf

app = FastAPI()
content_store = {}

class Query(BaseModel):
    query: str

@app.post("/generate")
async def generate_report(request: Query):
    try:
        questions = generate_questions(request.query)
        print('test')
        data = gather_data(questions)
        print('test')
        analysis = analyze_data(data)
        print('test')
        content_store["preview"] = analysis
        report_path = generate_pdf(request.query, analysis)
        print('test')
        return {"url": report_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/preview")
async def preview_report():
    try:
        return {"content": content_store.get("preview", "No content available.")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
