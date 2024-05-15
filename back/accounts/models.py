from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Genre

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='liked_users')
    like_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)