from django.db import models

# Create your models here.
class Planet(models.Model):
    """
        Model for managing the planets
    """
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'planet'
        verbose_name = 'Planet'
        verbose_name_plural = 'Planets'
    
    def __str__(self) -> str:
        return self.name


class City(models.Model):
    """
        Model for managing the Cities
    """
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
    
    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    """
        Model for managing the Locations that a Spaceship can Travel to 
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    capacity = models.DecimalField(max_digits=5, decimal_places=0)

    class Meta:
        db_table = 'location'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self) -> str:
        return f'{self.city.name}, {self.planet.name}'


class Spaceship(models.Model):
    """
        Model for managing the Spaceships
    """
    Decommissioned = 'DE'
    Maintenance = 'MA'
    Operational = 'OP'
    
    # Defining the status of Spaceships
    STATUS = (
        (Decommissioned, 'Decommissioned'),
        (Maintenance, 'Maintenance'),
        (Operational, 'Operational') 
        )

    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default=Decommissioned)

    class Meta:
        db_table = 'spaceship'
        verbose_name = 'Spaceship'
        verbose_name_plural = 'Spaceships'

    def __str__(self) -> str:
        return self.name
    
    def travel(self, destination):
        """
            Travel implemented in model level to conform with DRY.
        """
        travel_completed = False
        if destination.capacity > 0:
            old_location = self.location
            old_location.capacity -= 1
            destination.capacity += 1
            self.location = destination
            old_location.save()
            destination.save()
            self.save()
            travel_completed = True
        
        return travel_completed