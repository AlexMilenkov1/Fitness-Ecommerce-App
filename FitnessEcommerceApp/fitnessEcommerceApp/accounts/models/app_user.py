from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from fitnessEcommerceApp.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=20,
        blank=False,
        null=False,
        unique=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    USERNAME_FIELD = "email"

    objects = AppUserManager()