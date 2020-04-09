from rest_framework import serializers
from .models import Document, Exercise, User, ExerciseAttempt


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'author')


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'document_id', 'paragraph_index', 'paragraph_start',
                  'sentence_index', 'sentence_text', 'topic_words')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')


class ExerciseAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseAttempt
        fields = ('id', 'exercise_id', 'user_id', 'topic_word_index',
                  'exercise_type', 'guess', 'answer', 'is_correct')
