from django.contrib.auth import get_user_model
from django.db import models
from fitnessEcommerceApp.products.models import Product

UserModel = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='cart'
    )

    products = models.ManyToManyField(Product, through='CartItem', related_name='carts')


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"


# Create your models here.
class Order(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='order'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_paid = models.BooleanField(
        default=False,
    )

    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        related_name='order'
    )
