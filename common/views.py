from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import (
    DocumentSerializer,
    ExerciseSentenceSerializer,
    UserSerializer,
    ExerciseAttemptSerializer
)
from .models import(
    Document,
    ExerciseSentence,
    User,
    ExerciseAttempt
)


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
