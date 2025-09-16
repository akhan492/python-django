from django.urls import path
from . import views
urlpatterns = [
    # path('', views.all_chai, name='all_home'), 
    path('api/movies/', views.movie_list, name='all_movies'), 
    path('api/movies/<int:pk>', views.movies_details, name='movie-details'), 
]
