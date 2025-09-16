from watchlist_app.models import WatchList, StreamPlatform
from rest_framework import serializers



class WatchListSerializer(serializers.ModelSerializer):
   class Meta:
      model = WatchList
      fields= '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
   watchlist = WatchListSerializer(many=True, read_only=True)
   class Meta:
      model =StreamPlatform
      fields= '__all__'
      