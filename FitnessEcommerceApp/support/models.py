from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class SupportTicket(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

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

    email = models.EmailField(
        max_length=254,
        blank=False,
        null=False,
    )

    is_resolved = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ('can_resolve_tickets', 'Can resolve tickets')
        ]
