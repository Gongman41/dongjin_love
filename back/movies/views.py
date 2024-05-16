from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Review
from .serializers import MovieSerializer, MovieListSerializer
from .serializers import ReviewSerializer, ReviewListSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET'])
def movies(request):
  # 전체 영화 조회
  movies = get_list_or_404(Movie)
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def detail(request, movie_id):
  # 단일 영화 조회
  movie = get_object_or_404(Movie, pk=movie_id)
  serializer = MovieSerializer(movie)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def review(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  # 전체 리뷰 조회
  if request.method == 'GET':
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  # 해당 영화의 리뷰 작성
  if request.method == 'POST':
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(movie=movie, user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST', 'PUT'])
def review_detail(request, movie_id, review_id):
  review = get_object_or_404(Review, pk=review_id)
  # 리뷰 삭제
  if request.method == 'POST':
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  # 리뷰 수정
  elif request.method == 'PUT':
    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
  
  
