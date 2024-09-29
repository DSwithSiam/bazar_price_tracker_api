from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
   
        account.set_password(password)
        
        account.save()
        
        return account



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                return data
            raise serializers.ValidationError("Incorrect username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
       

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'username', 'market_id', 'role', 'email', 'phone', 'profile_picture']
