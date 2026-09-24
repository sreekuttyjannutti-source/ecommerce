from django.conf import settings
from django.db import models
<<<<<<< HEAD
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL
class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def _str_(self):
        return f"Cart of {self.user}"
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def _str_(self):
        return f"{self.product.name} ({self.quantity})"

=======
from products.models import Product
class Cart(models.Model): 
user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
class CartItem(models.Model): 
cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items') 
product = models.ForeignKey(Product, on_delete=models.CASCADE) quantity = models.PositiveIntegerField(default=1) class Meta: constraints = [models.UniqueConstraint(fields=['cart','product'], name='unique_cart_product')]
>>>>>>> 5d8743328ea89c3fcd21f1d0001362317ae68446
