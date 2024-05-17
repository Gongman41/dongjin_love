from django.shortcuts import get_object_or_404
from .models import Movie, Review
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

@api_view(['GET','POST'])
def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        pass
