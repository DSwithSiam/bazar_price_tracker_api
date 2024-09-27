from rest_framework import viewsets
from .models import MarketManager, CustomUser
from .serializers import MarketManagerSerializer, CustomUserSerializer, LoginSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework import status



class MarketManagerViewSet(viewsets.ModelViewSet):
    queryset = MarketManager.objects.all()
    serializer_class = MarketManagerSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data  # This should be a MarketManager instance
            login(request, user)  # Log the user in
            
            
            return Response({
                "message": "Login successful",
                "username": user.username,
                "user_id": user.id,
               
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)