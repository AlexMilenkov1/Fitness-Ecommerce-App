from django.db import models

from fitnessTracker.goals.models import Goal


# Create your models here.
class Progress(models.Model):
    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        related_name="progress_updates"
    )

    date = models.DateField(
        auto_now_add=True
    )

    current_value = models.FloatField()  # e.g., current weight, distance, etc.

    notes = models.TextField(
        null=True,
        blank=True
    )

