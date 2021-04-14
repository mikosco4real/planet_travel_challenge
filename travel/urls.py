from django.urls import path, include
from rest_framework import routers
from .views import PlanetViewset, CityViewset, LocationViewset, SpaceshipViewset

router = routers.DefaultRouter(trailing_slash=False)
router.register('planet', PlanetViewset, 'planet_api')
router.register('city', CityViewset, 'city_api')
router.register('location', LocationViewset, 'location_api')
router.register('spaceship', SpaceshipViewset, 'spaceship_api')

urlpatterns = [
    path('', include(router.urls), name='root_api'),
]