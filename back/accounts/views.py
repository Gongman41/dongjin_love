from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Review
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def profile(request, user_id):
  pass