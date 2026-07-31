from django.urls import path

from quizzes.api.views import QuizCreateView

urlpatterns = [
    path("quizzes/", QuizCreateView.as_view(), name="quiz-create"),
]
