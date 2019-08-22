from django.db import models


# Create your models here.
class Dj(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    image = models.ImageField()


class Chef(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    image = models.ImageField()





