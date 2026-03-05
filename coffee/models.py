from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField(max_length=2083)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.coffee.price * self.quantity
