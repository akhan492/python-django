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
    

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  # save **once** after updating all fields
        return instance