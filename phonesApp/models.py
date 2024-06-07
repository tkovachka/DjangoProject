from django.contrib.auth.models import User
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    isInEU = models.BooleanField()

    def __str__(self):
        return self.name


# Create your models here.
class Phone (models.Model):
    TYPE = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    ]

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=7, choices=TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='phones/')
    price = models.IntegerField()
    year = models.IntegerField()
    isNew = models.BooleanField()

    def __str__(self):
        return f"{self.manufacturer} - {self.model}"

