from django.contrib.auth.models import User
from rest_framework import serializers, permissions

from .models.document import Document
from .models.exercise_sentence import ExerciseSentence
from .models.exercise_attempt import ExerciseAttempt


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'author')
        permission_classes = [permissions.IsAuthenticated]


class ExerciseSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSentence
        fields = ('id', 'document', 'paragraph_index', 'paragraph_start',
                  'sentence_index', 'sentence_text', 'topic_words')
        permission_classes = [permissions.IsAuthenticated]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        permission_classes = [permissions.IsAuthenticated]


class ExerciseAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseAttempt
        fields = ('id', 'exercise', 'user', 'topic_word_index',
                  'exercise_type', 'guess', 'answer', 'is_correct')
        permission_classes = [permissions.IsAuthenticated]
