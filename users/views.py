from rest_framework import viewsets
from .models import UserProfile
from .serializers import RegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token

class UserRegistrationApiView(APIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            token = default_token_generator.make_token(user)
            
            UserProfile.objects.create(user=user, email= user.email)
             
            return Response("Wellcome")
        return Response(serializer.errors)


class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
    
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)
    
class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.user.username
        if username:
            queryset = queryset.filter(username=username)
        return queryset

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(user=user)
        return queryset