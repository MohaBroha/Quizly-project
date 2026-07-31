from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ai.services.quiz_service import QuizService
from quizzes.models import Quiz
from quizzes.api.serializers import (
    QuizCreateSerializer,
    QuizSerializer,
)


class QuizCreateView(generics.GenericAPIView):
    """
    Creates a new quiz from a YouTube URL.
    """

    serializer_class = QuizCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Quiz.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quiz = QuizService.create_quiz(
            request.user,
            serializer.validated_data["url"],
        )

        return Response(
            QuizSerializer(quiz).data,
            status=status.HTTP_201_CREATED,
        )
