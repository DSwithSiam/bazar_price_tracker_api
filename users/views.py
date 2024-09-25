from rest_framework import viewsets
from .models import MarketManager, CustomUser
from .serializers import MarketManagerSerializer, CustomUserSerializer

class MarketManagerViewSet(viewsets.ModelViewSet):
    queryset = MarketManager.objects.all()
    serializer_class = MarketManagerSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
