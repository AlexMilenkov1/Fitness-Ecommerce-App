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
        blank=False
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=False
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=False
    )

    height = models.FloatField(
        help_text="Height in cm",
        null=True,
        blank=False
        )

    weight = models.FloatField(
        help_text="Weight in kg",
        null=True,
        blank=False
    )

    profile_picture = models.ImageField(
        upload_to='profile_images',
        null=True,
        blank=True
    )

    active_profile = models.BooleanField(
        default=False,
    )
