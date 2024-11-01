from django.db import models


# Create your models here.
class Goal(models.Model):
    goal_title = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    target_value = models.FloatField(
        null=True,
        blank=True
    )

    start_date = models.DateField(
        auto_now_add=True,
    )

    end_date = models.DateField()

    achieved = models.BooleanField(
        default=False
    )
