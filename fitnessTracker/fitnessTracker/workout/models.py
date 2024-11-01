from django.db import models

from fitnessTracker.workout.choices import ExerciseTypes


# Create your models here.
class Workout(models.Model):
    exercise_type = models.CharField(
        null=False,
        blank=False,
        choices=ExerciseTypes.choices
    )

    duration = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    calories_burned = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    date = models.DateField(auto_now_add=True)


