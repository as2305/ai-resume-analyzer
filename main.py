from fastapi import FastAPI, UploadFile
from analyze import analyze_pdf
import os
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile, title:str):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    result = analyze_pdf(temp_path, title)
    return PlainTextResponse(content=result)