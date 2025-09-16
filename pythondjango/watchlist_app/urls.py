from django.urls import path
from . import views
urlpatterns = [
    # path('', views.all_chai, name='all_home'), 
    path('list/', views.WatchListAV.as_view(), name='movie-list'), 
    path('<int:pk>', views.MovieDetailsAV.as_view(), name='movie-details'), 
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'), 
]
