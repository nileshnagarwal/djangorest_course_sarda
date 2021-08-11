from rest_framework import request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Movie
from .serializers import MovieSerializer

@api_view()
def movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)