import os
from google import genai
import asyncio
import edge_tts
from key import gemini_key

model = "gemini-2.5-flash"
key = gemini_key

def analyze_pdf(file, job_title):
    prompt = f"""
    You are an expert, strict HR Manager specializing in recruiting **{job_title}** professionals. 

    Analyze this resume strictly against the core qualifications of a {job_title}. 
    Do not be polite or soft. If the resume is completely irrelevant to the target role, give it a realistic score of 0 out of 10 and explicitly state the misalignment.

    Provide:
    1. An objective overall suitability rating out of 10.
    2. 3 bullet points about their strengths (if any are transferable, otherwise note the gaps).
    3. 3 points for critical improvement to match this target industry.

    The output will be used by an executive recruiter to instantly filter out unqualified applicants.
    Keep the tone human-like and friendly.
    """
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

