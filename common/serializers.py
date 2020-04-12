from rest_framework import serializers, permissions
from .models import Document, ExerciseSentence, User, ExerciseAttempt


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
        fields = ('id', 'name', 'email', 'password')
        permission_classes = [permissions.IsAuthenticated]


class ExerciseAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseAttempt
        fields = ('id', 'exercise', 'user', 'topic_word_index',
                  'exercise_type', 'guess', 'answer', 'is_correct')
        permission_classes = [permissions.IsAuthenticated]
