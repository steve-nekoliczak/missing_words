from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    def get_serializer_class(self):
        if self.action == 'exercise_attempts':
            return ExerciseAttemptSerializer
        else:
            return self.serializer_class

    @action(detail=True, methods=['get'])
    def exercise_attempts(self, request, pk=None):
        user = self.get_object()
        exercise_attempts = user.exercise_attempts.all()
        serializer = self.get_serializer(exercise_attempts, many=True)
        return Response(serializer.data)


class ExerciseAttemptViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseAttemptSerializer
    queryset = ExerciseAttempt.objects.all()
