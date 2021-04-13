from rest_framework.serializers import ModelSerializer
from .models import Planet, City, Location, Spaceship

# Define the Serializers for the Travel Models

class PlanetSerializer(ModelSerializer):

    class Meta:
        model = Planet
        fields = '__all__'

class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
        depth = 1


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'
        depth = 2


class SpaceshipSerializer(ModelSerializer):

    class Meta:
        model = Spaceship
        fields = '__all__'
        depth = 3