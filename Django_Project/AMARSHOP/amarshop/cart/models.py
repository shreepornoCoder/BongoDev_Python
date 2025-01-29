from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility methods
    def get_total_price(self):
        return sum(item.get_price() for item in self.items.all())
    
    def get_total_item(self):
        return sum(item.quantity for item in self.items.all())

class CartItems(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="product")
    quantity = models.BigIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility methods
    def get_price(self):
        return self.product.price * self.quantity
    
    class Meta:
        unique_together = ['cart', 'product']
    
class Saved_Items(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="saved_items")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="saved_product")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']