from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
        null=True
    )


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
    )

    in_stock = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

