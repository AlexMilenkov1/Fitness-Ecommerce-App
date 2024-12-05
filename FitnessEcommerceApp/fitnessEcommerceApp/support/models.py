from django.db import models
from django.utils import timezone


# Create your models here.
class SupportTicket(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    message = models.TextField(
        blank=False,
        null=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_resolved = models.BooleanField(
        default=False
    )


class Response(models.Model):
    ticket = models.ForeignKey(SupportTicket, related_name="responses", on_delete=models.CASCADE)

    message = models.TextField()

    created_at = models.DateTimeField(
        default=timezone.now
    )