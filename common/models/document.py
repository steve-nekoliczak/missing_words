from django.db import models


class Document(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.TextField()
    author = models.TextField()
    class Meta:
        db_table = 'documents'

