from django.db import models

# Create your models here.

# def products(m)

class Categories(models.Model):
    name = models.CharField(
        primary_key=True,
        blank=False,
        max_length=50,
        
        )
    
    def __str__(self):
        return self.name

class Multivitamins(models.Model):
    name = models.CharField(
        max_length=30, 
        blank=False, 
        primary_key=True)
    description = models.TextField(max_length=200)
    # category = models.ForeignKey(
    #     Categories, 
    #     null=True,
    #     on_delete=models.CASCADE
    #     )


    def __str__(self):
        return (self.name)
    




