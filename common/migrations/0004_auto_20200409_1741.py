# Generated by Django 3.0.5 on 2020-04-09 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20200409_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='document_id',
            new_name='document',
        ),
        migrations.RenameField(
            model_name='exerciseattempt',
            old_name='exercise_id',
            new_name='exercise',
        ),
        migrations.RenameField(
            model_name='exerciseattempt',
            old_name='user_id',
            new_name='user',
        ),
    ]
