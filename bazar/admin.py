from django.contrib import admin
from .models import Market, Item, Price

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('market', 'item', 'price_per_kg', 'last_updated')
    list_filter = ('market', 'item')
