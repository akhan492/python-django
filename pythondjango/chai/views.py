from django.shortcuts import render
from chai.models import Movies
from django.http import Http404, JsonResponse
# Create your views here.
def all_chai(request):
  return  render(request, "chai/index.html", {'chais': [{
    'name': "arsalan",
    'age': 28,
  }]})

def movie_list(request):
  movies = Movies.objects.all()
  data = {
    'movies' : list(movies.values())
  }
  return JsonResponse(data)



def movies_details(request, pk):
    
    try:
        movie = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        raise Http404("Movie not found")

    data = {
        'name': movie.name,
        'description': movie.description, 
        'active': movie.active
    }
    return JsonResponse(data)
    
