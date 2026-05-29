import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_meeting(transcript):

    prompt = f"""
    Analyze the following meeting transcript.

    Provide:

    1. Executive Summary
    2. Key Discussion Points
    3. Action Items
    4. Important Decisions

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)

    return response.text