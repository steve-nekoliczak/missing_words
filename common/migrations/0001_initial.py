# Generated by Django 3.0.5 on 2020-04-09 16:33

import django.contrib.postgres.fields.citext
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document_title', models.TextField()),
                ('document_author', models.TextField()),
            ],
            options={
                'db_table': 'documents',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paragraph_index', models.IntegerField()),
                ('paragraph_start', models.BooleanField()),
                ('sentence_index', models.IntegerField()),
                ('sentence_text', django.contrib.postgres.fields.jsonb.JSONField()),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Document')),
            ],
            options={
                'db_table': 'exercises',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('email', django.contrib.postgres.fields.citext.CIEmailField(max_length=254)),
                ('password', models.TextField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='ExerciseAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('topic_word_index', models.IntegerField()),
                ('exercise_type', models.TextField()),
                ('guess', models.TextField()),
                ('answer', models.TextField()),
                ('is_correct', models.BooleanField()),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Exercise')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.User')),
            ],
            options={
                'db_table': 'exercise_attempts',
            },
        ),
    ]