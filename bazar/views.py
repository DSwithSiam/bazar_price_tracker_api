from rest_framework import viewsets
from .models import Market, Item, Price
from .serializers import MarketSerializer, ItemSerializer, PriceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Price
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@api_view(['GET'])
def compare_prices(request):
    item_name = request.query_params.get('item')
    market_ids = request.query_params.getlist('markets')
    prices = Price.objects.filter(item__name=item_name, market__id__in=market_ids)
    return Response({'prices': PriceSerializer(prices, many=True).data})


@api_view(['GET'])
def price_history(request, item_id):
    prices = Price.objects.filter(item__id=item_id).order_by('-last_updated')
    return Response({'history': PriceSerializer(prices, many=True).data})

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    


