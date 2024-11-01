from django.db import models


class ExerciseTypes(models.TextChoices):
    CARDIO = 'cardio', 'cardio'
    STRENGTH = 'strength', 'strength'
    FLEXIBILITY = 'flexibility', 'flexibility'
    BALANCE = 'balance', 'balance'
    ENDURANCE = 'endurance', 'endurance'
