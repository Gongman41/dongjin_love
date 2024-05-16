from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Review, User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET','POST'])
def profile(request, user_id):
  user = get_object_or_404(User, pk = user_id)
  if request.method == 'GET':
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
