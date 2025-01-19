from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, validators=[MinLengthValidator(0), MaxLengthValidator(5)])
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, default="N/A")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="category")
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, related_name="brand")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image_url = models.URLField()
    alt_text = models.CharField(max_length=150)
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE, related_name="images")
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
