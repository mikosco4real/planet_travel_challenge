# Planet Travel Challenge
---
In the distant future, humans have colonised all 8 planets in our solar system. You work for Stomble, a shipping company trying to expand their operations to the whole solar system. You have been asked to develop a system to manage the logistics of Stomble’s fleet of spaceships.  

## Requirements 
You will develop a REST API which will store information about the location of the spaceships, as well as the locations in which they are stationed.   In order to accomplish this, your API must fulfill the following use cases:  
* Add spaceships: a spaceship must have an id, name, model, location (made up of a city and a planet) and its status (decommissioned, maintenance or operational).  Update the spaceship status: to one of the 3 possible states.  
* Add a location: a location must have an id, city name and a planet name; as well as the spaceport capacity (how many spaceships can be stationed at this location simultaneously).  
* Remove spaceships: given a spaceship’s id.  
* Remove location: given a location’s id.  
* Travel functionality: Travel involves changing the location of the spaceship and adjusting the capacity of the source and destination spaceports. Before carrying out the travel transaction, check these two factors:  The spaceport capacity of the destination (if not, return an appropriate error).  The status of the spaceship (only operational spaceships can travel).

## Project Setup
---
1. Clone the project into a directory
2. Create a virtual environment
3. Activate the virtual Environment
4. Install the requirements.txt file - ``` pip install -r requirements.txt ```
5. Make migrations - ``` python manage.py makemigrations ```
6. Migrate - ``` python manage.py migrate ```

## Dependencies
You require python 3.8 or higher for a stable experience

## TESTS
This project follows Test Driven Development Principles(TDD). Please run the test to make sure that everything is working fine using the command:
``` python manage.py test ```

## RUN the Developement Server
If the test works out fine with no Failures, You need to run the development server on one of your terminal or CMD prompt
``` python manage.py runserver ```
User your browser to be able to access the program using the browsable api, This way you could see all the endpoints and can interact with it.
If you are however testing this with postman, then checkout the api documentation below.

# API Documentation
The works with four different objects some of which relate to each other in some ways. They include:
1. **Planet:** - *For creating/managing Planet names*
2. **City**    - *For creating/managing cities* Links to Planet
3. **Location** - *For creating/managing travelable locations* Links to Planet and City
4. **Spaceship** - *For creating/managing Spaceships* Links to Location

## Planet object and Examples

**End Point** = ``` http://127.0.0.1:8000/planet ```

Attributes = id, name

* To create a planet, make a post request to the endpoint. Eg:
``` post(url='http://127.0.0.1:8000/planet', data={'name': "Earth"}) ``` - *creates a planet called "Earth" with an id of 1* ID is autogenerated
* To get all the planets created, make a get request to the endpoint. eg.
``` get(url='http:127.0.0.1:8000/planet') ```
* For Retrieve/update/delete you need to provide the number of the target object in the url. eg.
``` put/patch/delete/get(url=url='http://127.0.0.1:8000/planet/1', data={'name': "Pluto"}) ```


## City object and Examples

**End Point** = ``` http://127.0.0.1:8000/city ```

Attributes = id, name, planet

* To create a city, make a post request to the endpoint. Eg:
``` post(url='http://127.0.0.1:8000/city', data={'name': "Sydney", 'planet': 1}) ``` - *creates a city called "Sydney" with planet_id of 1 and an id of 1* ID is autogenerated
* To get all the cities created, make a get request to the endpoint. eg.
``` get(url='http:127.0.0.1:8000/city') ```
* For Retrieve/update/delete you need to provide the number of the target object in the url. eg.
``` put/patch/delete/get(url=url='http://127.0.0.1:8000/city/1', data={'name': "Sydney", 'planet': 1}) ```


## Location object and Examples

**End Point** = ``` http://127.0.0.1:8000/location ```

Attributes = id, city, planet, capacity

* To create a location, make a post request to the endpoint. Eg:
``` post(url='http://127.0.0.1:8000/location', data={'planet': 1, 'city': 1, 'capacity': 2}) ``` - *creates a location with city = "Sydney", planet = "Earth with an id of 1* ID is autogenerated
* To get all the locations created, make a get request to the endpoint. eg.
``` get(url='http:127.0.0.1:8000/location') ```
* For Retrieve/update/delete you need to provide the number of the target object in the url. eg.
``` put/patch/delete/get(url=url='http://127.0.0.1:8000/planet/1', data={'planet': 1, 'city': 1, 'capacity': 2}) ```


## Spaceship object and Examples

**End Point** = ``` http://127.0.0.1:8000/spaceship ```

Attributes = id, name, model, location, status

* To create a spaceship, make a post request to the endpoint. Eg:
``` post(url='http://127.0.0.1:8000/spaceship', data={'name': "Emirates", 'model': "AWK453", 'location': 1, 'status': "DE"}) ``` - *creates a spaceship called "Emirates" with an id of 1, model of "AWK453", Location of Sydney-Earth, status of Decommissioned* ID is autogenerated
* To get all the spaceships created, make a get request to the endpoint. eg.
``` get(url='http:127.0.0.1:8000/spaceship') ```
* For Retrieve/update/delete you need to provide the number of the target object in the url. eg.
``` put/patch/delete/get(url=url='http://127.0.0.1:8000/spaceship/1', data={'name': "Emirates", 'model': "AWK453", 'location': 1, 'status': "DE"}) ```

## To Travel

**End Point** = ``` http://127.0.0.1/spaceship/<id>/travel ```

it accepts only post_request. and requires you to provide a destination as an input.

eg: post(url='http://127.0.0.1/spaceship/1/travel', data={'destination': 2}) *The destination is the ID of the Location you want to go*