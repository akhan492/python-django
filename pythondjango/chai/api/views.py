from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chai.models import Movies
from chai.api.serializers import MovieSerializer
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error_messages) #later will check with only errors


@api_view()
def movies_details(request, pk):
    try:
        movie = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        raise Http404("Movie not found")

    serilaizer = MovieSerializer(movie)
    return Response(serilaizer.data)