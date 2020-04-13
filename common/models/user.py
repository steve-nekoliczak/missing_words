from django.db import models
from django.contrib.postgres import fields


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    email = fields.CIEmailField()
    password = models.TextField()
    class Meta:
        db_table = 'users'
