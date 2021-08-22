from django.urls import path

from .views import *

urlpatterns = [
    path('list/', MovieList.as_view(), name='movies-list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie-detail')
]
