from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Genre, Review

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    lovepoint = models.IntegerField(default=0)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movie = models.ManyToManyField(Movie, on_delete=models.CASCADE, related_name='liked_users')
    like_genre = models.ManyToManyField(Genre, on_delete=models.CASCADE)
