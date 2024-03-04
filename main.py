from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from text_analysis import analyze_texts_in_directory
from fastapi.responses import RedirectResponse

app = FastAPI()

class AnalysisResult(BaseModel):
    total_words: int
    unique_words: int
    top_words: List[tuple]

@app.get("/analyze", response_model=AnalysisResult)
async def analyze(top_n: int = 10):
    try:
        analysis_results = analyze_texts_in_directory('./testfiles', top_n=top_n)
        return AnalysisResult(**analysis_results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/")
async def root():
    return RedirectResponse(url="/analyze?top_n=10")
