from ai.services.gemini_service import GeminiService

transcript = """
Python is a programming language.
It is widely used for web development and artificial intelligence.
"""

quiz = GeminiService.generate_quiz(transcript)

print(quiz["title"])
print(quiz["description"])
print(quiz["questions"])
