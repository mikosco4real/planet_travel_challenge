from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
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
        self.assertEqual(spaceship.location.capacity, 1)

        loc = Location.objects.get(id=1)
        loc.capacity = 0
        self.assertFalse(spaceship.travel(loc))
        self.assertEqual(spaceship.location.city.name, "Melbourne")


class TestAPIViews(APITestCase):
    def setUp(self) -> None:
        self.planet = {'name': "Earth"}
        self.planet2 = {'name': "Jupyter"}
        self.city = {'name': "Sydney", 'planet': 1}
        self.city2 = {'name': "Melbourne", 'planet': 2}
        self.location = {'planet': 1, 'city': 1, 'capacity': 2}
        self.location2 = {'planet': 2, 'city': 2, 'capacity': 0}
        self.spaceship = {'name': "Emirates", 'model': "AWK453", 'location': 1, 'status': "DE"}
        return super().setUp()

    def test_planet_api(self):
        response = self.client.post('/planet', self.planet) # Make a post request to the api endpoint
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        result = self.client.get('/planet/1') # Confirm that you can get the added item back
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        delete_item = self.client.delete('/planet/1') # Confirm that you can delete the item
        self.assertEqual(delete_item.status_code, status.HTTP_204_NO_CONTENT)

        result = self.client.get('/planet/1') # Confirm that this item can no longer be found
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_city_api(self):
        self.client.post('/planet', self.planet)
        response = self.client.post('/city', self.city) # Make a post request to the api endpoint
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        result = self.client.get('/city/1') # Confirm that you can get the added item back
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        delete_item = self.client.delete('/city/1') # Confirm that you can delete the item
        self.assertEqual(delete_item.status_code, status.HTTP_204_NO_CONTENT)

        result = self.client.get('/city/1') # Confirm that this item can no longer be found
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_location_api(self):
        self.client.post('/planet', self.planet)
        self.client.post('/city', self.city)
        response = self.client.post('/location', self.location) # Make a post request to the api endpoint
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        result = self.client.get('/location/1') # Confirm that you can get the added item back
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        delete_item = self.client.delete('/location/1') # Confirm that you can delete the item
        self.assertEqual(delete_item.status_code, status.HTTP_204_NO_CONTENT)

        result = self.client.get('/location/1') # Confirm that this item can no longer be found
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_spaceship_api(self):
        self.client.post('/planet', self.planet)
        self.client.post('/city', self.city)
        self.client.post('/location', self.location)
        response = self.client.post('/spaceship', self.spaceship) # Make a post request to the api endpoint
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        result = self.client.get('/spaceship/1') # Confirm that you can get the added item back
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        result = self.client.put('/spaceship/1', {'name': "Emirates", 'model': "AWK453", 'location': 1, 'status': "OP"}) # Test that you can update spaceship details
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        spaceship = Spaceship.objects.get(id=1)
        self.assertEqual(spaceship.status, "OP")
        
        result = self.client.patch('/spaceship/1', {'status': "MA"}) # Test that you can update the status
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        spaceship = Spaceship.objects.get(id=1)
        self.assertEqual(spaceship.status, "MA")

        delete_item = self.client.delete('/spaceship/1') # Confirm that you can delete the item
        self.assertEqual(delete_item.status_code, status.HTTP_204_NO_CONTENT)

        result = self.client.get('/spaceship/1') # Confirm that this item can no longer be found
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_spaceship_travel(self):
        self.client.post('/planet', self.planet)
        self.client.post('/planet', self.planet2)
        self.client.post('/city', self.city)
        self.client.post('/city', self.city2)
        self.client.post('/location', self.location)
        self.client.post('/location', self.location2)
        self.client.post('/spaceship', self.spaceship)

        response = self.client.post('/spaceship/1/travel', {"destination": 2})
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

        spaceship = Spaceship.objects.get(id=1)
        self.assertEqual(spaceship.location.id, 1)

        self.client.patch('/location/2', {'capacity': 2})

        response = self.client.post('/spaceship/1/travel', {"destination": 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        spaceship = Spaceship.objects.get(id=1)
        self.assertEqual(spaceship.location.id, 2)
        self.assertEqual(spaceship.location.capacity, 1)


