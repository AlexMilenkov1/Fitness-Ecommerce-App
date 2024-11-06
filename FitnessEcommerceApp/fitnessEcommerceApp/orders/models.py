from django.db import models

from fitnessEcommerceApp import settings
from fitnessEcommerceApp.products.models import Product


# Create your models here.
class Order(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_paid = models.BooleanField(
        default=False,
    )

    is_shipped = models.BooleanField(
        default=False,
    )

    shipping_address = models.TextField()

    products = models.ManyToManyField('Product', through='OrderItem', related_name='orders')


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"


class Cart(models.Model):
    products = models.ManyToManyField(Product, through='CartItem', related_name='carts')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


