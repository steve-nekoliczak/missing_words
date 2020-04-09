from django.db import models
from django.contrib.postgres import fields


class Document(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.TextField()
    author = models.TextField()
    class Meta:
        db_table = 'documents'


class Exercise(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    document_id = models.ForeignKey('Document', models.CASCADE)
    paragraph_index = models.IntegerField()
    paragraph_start = models.BooleanField()
    sentence_index = models.IntegerField()
    sentence_text = fields.JSONField()
    class Meta:
        db_table = 'exercises'


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
    exercise_id = models.ForeignKey('Exercise', models.CASCADE)
    user_id = models.ForeignKey('User', models.CASCADE)
    topic_word_index = models.IntegerField()
    exercise_type = models.TextField()
    guess = models.TextField()
    answer = models.TextField()
    is_correct = models.BooleanField()
    class Meta:
        db_table = 'exercise_attempts'
