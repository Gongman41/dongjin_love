# Generated by Django 4.2.8 on 2024-05-16 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_dongjin_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='dongjin_point',
        ),
    ]