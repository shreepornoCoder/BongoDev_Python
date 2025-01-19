from rest_framework import serializers
from . models import Brand, Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["created_at", "updated_at"]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ["created_at", "updated_at"]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ["created_at"]

class ProductListSerializer(serializers.ModelSerializer):
    primary_image = serializers.SerializerMethodField() 
    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]

    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary = True).first()
        if primary_image:
            return ProductImageSerializer(primary_image).data
        
        return None

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    images = ProductImage(many=True)
    class Meta:
        model = Product
        exclude = ["updated_at"]
