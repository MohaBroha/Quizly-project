from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ai.services.quiz_service import QuizService
from quizzes.models import Quiz
from quizzes.api.serializers import (
    QuizCreateSerializer,
    QuizSerializer,
)


class QuizListCreateView(generics.ListCreateAPIView):
    """
    Lists all quizzes of the authenticated user and creates new quizzes.
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Quiz.objects.filter(owner=self.request.user).order_by("-created_at")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return QuizCreateSerializer
        return QuizSerializer

    def create(self, request, *args, **kwargs):
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


class QuizDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieves and updates a single quiz of the authenticated user.
    """

    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Quiz.objects.filter(owner=self.request.user)
