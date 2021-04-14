from django.contrib import admin
from .models import Planet, City, Location, Spaceship

# Register your models here.
admin.site.register((Planet, City, Location, Spaceship))
