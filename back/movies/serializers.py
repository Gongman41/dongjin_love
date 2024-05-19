from rest_framework import serializers
from .models import Movie, Review

class MovieListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
  class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
      model = Review
      fields = ('content', 'rank', 'user', 'like_users', 'updated_at')
  reviews = ReviewListSerializer(read_only=True, many=True)
  class Meta:
    model = Movie
    fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = ('content', 'rank', 'user', 'like_users', 'updated_at')
    
class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = ('content', 'rank')
