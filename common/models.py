from django.db import models
from django.contrib.postgres import fields


class Document(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.TextField()
    author = models.TextField()
    class Meta:
        db_table = 'documents'


class ExerciseSentence(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    document = models.ForeignKey('Document', models.CASCADE)
    paragraph_index = models.IntegerField()
    paragraph_start = models.BooleanField()
    sentence_index = models.IntegerField()
    sentence_text = models.TextField()
    topic_words = fields.JSONField()
    class Meta:
        db_table = 'exercise_sentences'


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    email = fields.CIEmailField()
    password = models.TextField()
    class Meta:
        db_table = 'users'


class ExerciseAttempt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    exercise = models.ForeignKey('ExerciseSentence', models.CASCADE)
    user = models.ForeignKey('User', models.CASCADE)
    topic_word_index = models.IntegerField()
    exercise_type = models.TextField()
    guess = models.TextField()
    answer = models.TextField()
    is_correct = models.BooleanField()
    class Meta:
        db_table = 'exercise_attempts'
