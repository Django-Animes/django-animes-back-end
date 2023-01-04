from django.db import models
from .models import User


class Achievement(models.Model):
    class Meta:
        ordering = ("id",)
        name = models.CharField(max_length=255)
        url = models.CharField(max_length=255)
        type_of_achievement = models.CharField(max_length=255)
        users = models.ManyToManyField(
            User,
            through="achievement_user",
            related_name="achievements",
        )
