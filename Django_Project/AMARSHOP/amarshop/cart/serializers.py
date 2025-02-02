from rest_framework import serializers
from .models import Cart, CartItems, Saved_Items
from products.serializers import ProductListSerializer
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    price = serializers.DecimalField(decimal_places=2, read_only=True, source='get_price')

    class Meta:
        model = CartItems
        fields = ['id', 'product', 'product_id', 'quantity', 'price']
        read_only_fields = ['id', 'price']

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be set atleast 1!") 
        raise value
    
    def validate_stock(self, data):
        product_id = self.data.get('product_id')
        quantity = self.data.get('quantity')

        try:
            product = Product.objects.get(id=product_id)
            if quantity > product.stock:
                raise serializers.ValidationError(f"Only {product.stock} is available in the stock!")
        except Product.DoesNotExist:
            raise serializers.ValidationError(f"Product doesn't found!")
        
        return data
    
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(decimal_places=2, read_only=True, source = 'get_total_price')
    total_quantity = serializers.IntegerField(read_only=True, source = 'get_total_quantity')

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price', 'total_quantity']

class SavedItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Saved_Items
        fields = ['id', 'product', 'product_id']