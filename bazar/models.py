from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)

class Price(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateField(auto_now=True)
