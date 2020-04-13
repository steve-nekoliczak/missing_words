from django.db import models
from django.contrib.postgres import fields


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
