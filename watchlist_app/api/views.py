from rest_framework import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from ..models import Movie
from .serializers import MovieSerializer

@api_view(['GET', 'POST'])
def movies_list(request):
    if (request.method == 'GET'):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    if (request.method == 'POST'):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'Error': 'Movie not found'}, status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):        
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    if (request.method == 'PUT'):
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    if (request.method == 'DELETE'):
        movie.delete()
        return Response(status.HTTP_204_NO_CONTENT)
