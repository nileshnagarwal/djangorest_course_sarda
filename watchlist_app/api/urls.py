from django.urls import path

from .views import *

urlpatterns = [
    path('list/', movies_list, name='movies-list'),
    path('<int:pk>/', movie_detail, name='movie-detail')
]
