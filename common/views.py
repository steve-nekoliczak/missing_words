from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import (
    DocumentSerializer,
    ExerciseSerializer,
    UserSerializer,
    ExerciseAttemptSerializer
)
from .models import(
    Document,
    Exercise,
    User,
    ExerciseAttempt
)


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ExerciseAttemptViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseAttemptSerializer
    queryset = ExerciseAttempt.objects.all()
