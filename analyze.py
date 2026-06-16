import os
from google import genai

model = "gemini-3.5-flash"
key = 

def analyze_pdf(file, job_title):
    prompt = f"You are an expert HR Manager with years of experience in {job_title}. Analyze this resume and give 3 points to improvement. "
    client = genai.Client(api_key=key)
    pdf = client.files.upload(file=file)
    response = client.models.generate_content(
        model=model,
        contents=[pdf, prompt]
    )
    print(response.text)

user_input = input("Enter file name: ")
title = input("Enter target job title: ")
analyze_pdf(user_input, title)