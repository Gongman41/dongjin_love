from django.shortcuts import render
from .models import Movie
# Create your views here.
# 영화 제목으로 영화 코드 추출 후 상세검색으로 재검색. 이후 리턴값 모델에 저장