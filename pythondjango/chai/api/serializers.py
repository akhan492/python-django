from chai.models import Movies
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name= serializers.CharField()
    description= serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
     print(validated_data, 'data')
     return  Movies.objects.create(**validated_data)

