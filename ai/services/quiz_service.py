from quizzes.models import Question, Quiz
from ai.services.gemini_service import GeminiService
from ai.services.whisper_service import WhisperService


class QuizService:
    """
    Handles the quiz creation workflow.
    """

    @staticmethod
    def create_quiz(user, url):
        """
        Creates a quiz from a YouTube URL.
        """

        quiz_data = QuizService.generate_quiz_data(url)

        quiz = QuizService.create_quiz_instance(
            user,
            url,
            quiz_data["title"],
            quiz_data["description"],
        )

        QuizService.create_questions(
            quiz,
            quiz_data["questions"],
        )

        return quiz

    @staticmethod
    def generate_quiz_data(url):
        """
        Generates quiz data from a YouTube URL.
        """

        transcript = WhisperService.generate_transcript(url)

        return GeminiService.generate_quiz(transcript)

    @staticmethod
    def create_quiz_instance(user, url, title, description):
        """
        Creates a quiz instance.
        """

        return Quiz.objects.create(
            owner=user,
            title=title,
            description=description,
            video_url=url,
        )

    @staticmethod
    def create_questions(quiz, questions):
        """
        Creates questions for a quiz.
        """

        for question in questions:
            Question.objects.create(
                quiz=quiz,
                question_title=question["question_title"],
                question_options=question["question_options"],
                answer=question["answer"],
            )
