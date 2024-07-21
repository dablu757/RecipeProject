from django.db import models

class Car(models.Model):
    name = models.CharField()
    speed = models.ImageField()

