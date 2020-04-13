from rest_framework import viewsets

from ..serializers import ExerciseAttemptSerializer
from ..models.exercise_attempt import ExerciseAttempt


class ExerciseAttemptViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseAttemptSerializer
    queryset = ExerciseAttempt.objects.all()
