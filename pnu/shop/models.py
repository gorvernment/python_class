from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
#class GameUser(models.Model):
#    server = models.CharField(max_length=100, unique=True)

class Shop(models.Model):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(5)])
    desc = models.TextField(blank=True)
    address = models.CharField(max_length=50, blank=True)

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

