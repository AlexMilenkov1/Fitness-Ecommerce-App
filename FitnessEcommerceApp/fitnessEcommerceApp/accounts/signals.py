from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from fitnessEcommerceApp.accounts.models import AppProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def add_profile(sender, instance, created, **kwargs):
    if created:
        AppProfile.objects.create(user=instance)
