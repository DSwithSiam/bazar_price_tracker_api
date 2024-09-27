from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import MarketManager, CustomUser


class MarketManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Password should only be writable, not readable

    class Meta:
        model = MarketManager
        fields = ['id', 'username', 'market_name', 'role', 'email', 'phone', 'profile_picture', 'password', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MarketManager(**validated_data)
        user.set_password(password) 
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)  
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'address', 'phone', 'email', 'profile_picture', 'created_at', 'updated_at']





class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = MarketManager.objects.filter(username=username).first()

            if user and user.check_password(password):
                return user  # Return the user instance
            raise serializers.ValidationError("Incorrect username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")
