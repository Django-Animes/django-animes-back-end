from django.contrib.auth.models import AbstractUser
from django.db import models
from achievements.models import Achievement


class TypeUser(models.TextChoices):
    TYPE_BRONZE = "Bronze"
    TYPE_SILVER = "Silver"
    TYPE_GOLD = "Gold"
    TYPE_FREE = "Free"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    type = models.TextField(choices=TypeUser.choices, default=TypeUser.TYPE_FREE)
    achievements = models.ManyToManyField(
            Achievement,
            related_name="users",
        )
