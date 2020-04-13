from rest_framework import viewsets

from .serializers import (
    DocumentSerializer,
    ExerciseSentenceSerializer,
    UserSerializer,
    ExerciseAttemptSerializer
)
from .models.document import Document
from .models.exercise_sentence import ExerciseSentence
from .models.exercise_attempt import ExerciseAttempt
from .models.user import User


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class ExerciseSentenceViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSentenceSerializer
    queryset = ExerciseSentence.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ExerciseAttemptViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseAttemptSerializer
    queryset = ExerciseAttempt.objects.all()
