from rest_framework import serializers
from .models import MarketManager, CustomUser

class MarketManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketManager
        fields = ['id', 'username', 'market_name', 'role', 'email', 'phone', 'profile_picture', 'created_at', 'updated_at']



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'address', 'phone', 'email', 'profile_picture', 'created_at', 'updated_at']
