from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Genre, Review

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', null=True)
    like_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='liked_users', null=True)
    like_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)