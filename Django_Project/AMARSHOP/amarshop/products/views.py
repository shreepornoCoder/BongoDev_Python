from django.shortcuts import render
from . models import Category, Brand, Product, ProductImage
from . serializers import BrandSerializer, CategorySerializer, ProductListSerializer, ProductDetailSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from . filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]
    search_fields = ['name', 'description', 'brand__name', 'category__name']
    ordering_fields = ['price', 'rating']
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    def get_serializer_class(self):
        if self.action == "retrive":
            return ProductDetailSerializer
        return ProductListSerializer

    # serializer_class = P
    # permission_classes = [IsAuthenticated]