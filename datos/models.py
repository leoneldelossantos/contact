from django.db import models

# Create your models here.

class Datos (models.Model):
    name = models.CharField (max_length=100)
    number = models.FloatField()
    bool = models.BooleanField()
    