from django.shortcuts import render
from .serializers import UserSerializers, UserLoginSerializer, AddressSerializers 
from .models import User, Address
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate

# Create your views here.
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializers(data = request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh_token':str(refresh),
            'access_token':str(refresh.access_token),
            'user':serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data = request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email = email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh_token':str(refresh),
                'access_token':str(refresh.access_token),
                'user':UserSerializers(user).data
            })
        return Response({
            'error':'Invalid Credintials!',
        }, status=status.HTTP_401_UNAUTHORIZED) 
    return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

class UpdateProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializers

    def get_object(self):
        return self.request.user
    
class UpdateProfileView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializers

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)