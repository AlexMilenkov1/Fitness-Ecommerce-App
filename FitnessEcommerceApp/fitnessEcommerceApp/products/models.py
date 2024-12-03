from django.core.validators import MinValueValidator, MaxValueValidator
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

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=200,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
    )

    in_stock = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0, message='You need to enter a numer higher than 0!')
        ]
    )

    rating = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(5, message="You can't exceed the value of 5!")
        ]
    )

    image_url = models.ImageField(
        upload_to='products_photos',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

