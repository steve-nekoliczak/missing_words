# Generated by Django 3.0.5 on 2020-04-09 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='document_title',
            new_name='title',
        ),
    ]
