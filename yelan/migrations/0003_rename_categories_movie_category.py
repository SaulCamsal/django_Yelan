# Generated by Django 4.0.2 on 2023-05-19 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yelan', '0002_rename_category_movie_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='categories',
            new_name='category',
        ),
    ]
