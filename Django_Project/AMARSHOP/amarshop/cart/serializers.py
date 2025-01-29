from rest_framework import serializers
from .models import Cart, CartItems, Saved_Items
from products.serializers import ProductListSerializer

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['id', 'product', 'product_id', 'quantity', 'price']
        read_only_fields = ['id', 'price']