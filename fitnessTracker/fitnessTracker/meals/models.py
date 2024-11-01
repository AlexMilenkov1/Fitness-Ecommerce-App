from django.db import models

from fitnessTracker.meals.choices import MealTypeChoices


# Create your models here.
class Meal(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=70
    )

    calories = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    protein = models.FloatField(
        blank=False,
        null=False,
    )

    carbs = models.FloatField(
        blank=False,
        null=False,
    )

    fats = models.FloatField(
        blank=False,
        null=False,
    )

    meal_type = models.CharField(
        choices=MealTypeChoices.choices
    )

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.meal_type} on {self.date}'
