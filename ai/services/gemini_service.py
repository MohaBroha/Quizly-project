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

        print("Calling Gemini...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        print("Gemini response:", repr(response.text))

        return json.loads(response.text)

    @staticmethod
    def build_prompt(transcript):
        """
        Builds the prompt for Gemini.
        """

        return f"""
Create a quiz based on the following transcript.

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
"""
