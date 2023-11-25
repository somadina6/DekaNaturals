from django.db import models

# Create your models here.

# def products(m)

class Multivitamins(models.Model):
    name = models.CharField(
        max_length=30, 
        blank=False, 
        primary_key=True)
    description = models.CharField(max_length=200)

