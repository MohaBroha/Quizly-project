from rest_framework import serializers

from quizzes.models import Question, Quiz


class QuizCreateSerializer(serializers.Serializer):
    """
    Serializer for creating a new quiz from a YouTube URL.
    """

    url = serializers.URLField()


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for quiz questions.
    """

    class Meta:
        model = Question
        fields = (
            "id",
            "question_title",
            "question_options",
            "answer",
            "created_at",
            "updated_at",
        )


class QuizSerializer(serializers.ModelSerializer):
    """
    Serializer for quiz responses.
    """

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = (
            "id",
            "title",
            "description",
            "video_url",
            "created_at",
            "updated_at",
            "questions",
        )
