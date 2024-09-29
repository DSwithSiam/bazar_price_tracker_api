from django.db import models
from users.models import UserProfile


class Market(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=100)
    manager = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='market', blank=True, null=True)
    market_rules = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Call the original save method to create the market first
        super().save(*args, **kwargs)

        # Update the UserProfile's market_id if manager exists
        if self.manager:
            self.manager.market_id = str(self.id)  # Store the market ID as a string
            self.manager.save()

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

