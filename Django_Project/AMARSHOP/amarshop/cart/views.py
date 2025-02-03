from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from . models import Cart, CartItems, Saved_Items
from . serializers import CartSerializer, CartItemSerializer, SavedItemSerializer

class CartItemViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def get_or_create_cart(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)