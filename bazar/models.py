from django.db import models
from users.models import MarketManager


class Market(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=100)
    manager = models.OneToOneField(MarketManager, on_delete=models.CASCADE, related_name='market', blank=True, null=True)
    market_rules = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Price(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"Market: {self.market}, Item: {self.item}, Price(KG): {self.price_per_kg}"

