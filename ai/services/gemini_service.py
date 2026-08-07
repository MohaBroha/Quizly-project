import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiService:
    """
    Handles communication with Gemini.
    """

    @staticmethod
    def generate_quiz(transcript):
        """
        Generates quiz data from a transcript.
        """

        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        prompt = GeminiService.build_prompt(transcript)

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return json.loads(response.text)

    @staticmethod
    def build_prompt(transcript):
        """
        Builds the prompt for Gemini.
        """

        return f"""
Create a quiz based on the following transcript.

Generate exactly 10 multiple-choice questions.

Transcript:
{transcript}

Return ONLY valid JSON.

Structure:

{{
  "title": "...",
  "description": "...",
  "questions": [
    {{
      "question_title": "...",
      "question_options": [
        "...",
        "...",
        "...",
        "..."
      ],
      "answer": "..."
    }}
  ]
}}

Requirements:
- Generate exactly 10 questions.
- Each question must have exactly 4 answer options.
- Only one answer may be correct.
- The questions should cover different parts of the transcript.
"""
