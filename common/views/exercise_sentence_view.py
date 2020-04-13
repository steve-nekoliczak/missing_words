from rest_framework import viewsets

from ..serializers import ExerciseSentenceSerializer
from ..models.exercise_sentence import ExerciseSentence


class ExerciseSentenceViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSentenceSerializer
    queryset = ExerciseSentence.objects.all()
