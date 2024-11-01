from django.db import models


class MealTypeChoices(models.TextChoices):
    BREAKFAST = 'breakfast', 'breakfast'
    LUNCH = 'lunch', 'lunch'
    DINNER = 'dinner', 'dinner'
    SNACK = 'snack', 'snack'
