from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Planet, City, Location, Spaceship

# Create your tests here.
class TestTravelModels(TestCase):
    def setUp(self) -> None:
        planet = Planet.objects.create(name="Earth")
        city = City.objects.create(name="Sydney", planet=planet)
        Location.objects.create(city=city, planet=city.planet, capacity=20)
        return super().setUp()
    
    def test_add_location(self) -> None:
        city = City.objects.get(id=1)
        location = {'city': city, 'planet': city.planet, 'capacity': 20}
        loc = Location.objects.create(**location)
        self.assertEqual(loc.id, 2)
    
    def test_remove_location(self) -> None:
        city = City.objects.get(id=1)
        Location.objects.create(city=city, planet=city.planet, capacity=20)
        loc = Location.objects.get(id=1)
        loc.delete()
    
    def test_add_spaceship(self) -> None:
        loc = Location.objects.get(id=1)
        spaceship = Spaceship.objects.create(name="Emirates", model="AK467", location=loc)
        self.assertEqual(spaceship.id, 1)
        self.assertEqual(spaceship.status, 'DE')
    
    def test_spaceship_travel(self) -> None:
        spaceship = Spaceship.objects.create(name="Emirates", model="AK47", location=Location.objects.get(id=1))
        city = City.objects.create(name="Melbourne", planet=Planet.objects.get(id=1))
        destination = Location.objects.create(city=city, planet=city.planet, capacity=2)
        self.assertTrue(spaceship.travel(destination))
        self.assertEqual(spaceship.location.city.name, "Melbourne")

        loc = Location.objects.get(id=1)
        loc.capacity = 0
        self.assertFalse(spaceship.travel(loc))
        self.assertEqual(spaceship.location.city.name, "Melbourne")


class TestAPIViews(APITestCase):
    def setUp(self) -> None:
        return super().setUp()