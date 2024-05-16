from django.urls import path
from . import views


urlpatterns = [
    path('', views.movies),
    path('<int:movie_id>/', views.detail),
    path('<int:movie_id>/review/', views.review),
    path('<int:movie_id>/review/<int:review_id>/', views.review_detail),
]
