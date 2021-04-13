from travel.serializers import PlanetSerializer
from travel.models import Location, Planet
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PlanetSerializer, CitySerializer, LocationSerializer, SpaceshipSerializer
from .models import Planet, City, Location, Spaceship

# Create your views here.
class PlanetViewset(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = PlanetSerializer


class CityViewset(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = PlanetSerializer


class LocationViewset(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = PlanetSerializer


class SpaceshipViewset(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = PlanetSerializer