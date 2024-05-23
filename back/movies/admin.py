from django.contrib import admin
from .models import Genre, Person, Movie, Review

# Register your models here.
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Review)