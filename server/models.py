from django.db import models


# Create your models here.

class CarInfo(models.Model):
    number_photo = models.ImageField(blank=False)
