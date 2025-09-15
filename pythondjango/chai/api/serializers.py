from pythondjango.chai.models import Movies
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name= serializers.CharField()
    description= serializers.CharField()
    active = serializers.BooleanField()

    def create(self, valirm -rf .git        # Linux / macOS
# OR
rmdir /s /q .git   # Windows PowerShell / CMD
dated_data):
     return  Movies.objects.create(**validated_data)

