import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def summarize_meeting(transcript):

    prompt = f"""
You are an enterprise meeting intelligence assistant.

Analyze the following meeting transcript and generate a structured report.

Include:

# Executive Summary
Provide a concise overview of the meeting.

# Key Discussion Points
List the major topics discussed.

# Action Items
For each action item provide:
- Assignee
- Task
- Deadline (if mentioned)

# Important Decisions
List all final decisions made.

# Risks or Concerns Raised
Mention blockers, delays, dependencies or concerns.

# Next Steps
Mention the immediate follow-up actions.

# Overall Meeting Sentiment
Classify as:
Positive / Neutral / Negative

Transcript:
{transcript}
"""

    response = model.generate_content(prompt)

    return response.text