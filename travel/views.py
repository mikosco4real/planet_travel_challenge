from django.conf.urls import url
from travel.serializers import PlanetSerializer
from travel.models import Location, Planet
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers, serializers, status
from rest_framework.reverse import reverse
from .serializers import PlanetSerializer, CitySerializer, LocationSerializer, SpaceshipSerializer
from .models import Planet, City, Location, Spaceship

# Create your views here.
class PlanetViewset(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class CityViewset(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class LocationViewset(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class SpaceshipViewset(ModelViewSet):
    queryset = Spaceship.objects.all()
    serializer_class = SpaceshipSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer], url_path="travel", methods=["POST", "GET"])
    def travel(self, request, *args, **kwargs):
        spaceship = self.get_object()
        serializer = SpaceshipSerializer(spaceship)
        response_status = status.HTTP_400_BAD_REQUEST

        if request.POST:
            destination = request.POST["destination"]
        
            try:
                destination = Location.objects.get(id=destination)
            except Exception:
                destination = None
                response_status = status.HTTP_406_NOT_ACCEPTABLE
                return Response(data="The requested destination does not exist", status=response_status)
            
            if destination != None:
                travel = spaceship.travel(destination)
                if travel:
                    response_status = status.HTTP_200_OK
        return Response(data=serializer.data, status=response_status)