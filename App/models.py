from django.db import models

# Create your models here.
class Hostel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=50)
    vacancy = models.IntegerField()
    price = models.FloatField()
    image = models.CharField(max_length=2083, default='SOME STRING')