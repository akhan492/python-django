from watchlist_app.models import WatchList, StreamPlatform
from rest_framework import serializers


class StreamPlatformSerializer(serializers.ModelSerializer):
   class Meta:
      model =StreamPlatform
      fields= '__all__'

class WatchListSerializer(serializers.ModelSerializer):
   class Meta:
      model = WatchList
      fields= '__all__'
      