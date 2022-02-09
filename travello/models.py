from django.db import models
from django.forms import CharField

# Create your models here.
class Destinations(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
    promo= models.BooleanField(default=False)

class AllDestinations(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')