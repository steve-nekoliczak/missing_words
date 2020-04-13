from django.db import models
from django.conf import settings


class ExerciseAttempt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    exercise = models.ForeignKey('ExerciseSentence', models.CASCADE, related_name='exercise_attempts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='exercise_attempts')
    topic_word_index = models.IntegerField()
    exercise_type = models.TextField()
    guess = models.TextField()
    answer = models.TextField()
    is_correct = models.BooleanField()
    class Meta:
        db_table = 'exercise_attempts'
