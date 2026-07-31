class GeminiService:
    """
    Handles communication with Gemini.
    """

    @staticmethod
    def generate_quiz_data(url):
        """
        Generates quiz data from a YouTube URL.
        """

        transcript = "Temporary transcript."

        return GeminiService.generate_quiz(transcript)

    @staticmethod
    def build_prompt(transcript):
        """
        Builds the prompt for Gemini.
        """

        return f"""
Create a quiz based on the following transcript.

Transcript:
{transcript}

Return:
- title
- description
- questions
- four options per question
- correct answer
"""

    @staticmethod
    def mock_response():
        """
        Returns mock quiz data.
        """

        return {
            "title": "Test Quiz",
            "description": "Temporary quiz description.",
            "questions": [
                {
                    "question_title": "Temporary question",
                    "question_options": [
                        "Option A",
                        "Option B",
                        "Option C",
                        "Option D",
                    ],
                    "answer": "Option A",
                }
            ],
        }
