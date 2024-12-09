from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class AppProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    height = models.FloatField(
        help_text="Height in cm",
        null=True,
        blank=True
        )

    weight = models.FloatField(
        help_text="Weight in kg",
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to='profile_images',
        null=True,
        blank=True
    )

