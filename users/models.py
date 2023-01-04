from django.contrib.auth.models import AbstractUser
from django.db import models

class TypeUser(models.TextChoices):
    TYPE_BRONZE = 'Bronze'
    TYPE_SILVER = 'Silver'
    TYPE_GOLD = 'Gold'
    TYPE_FREE = 'Free'

class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    type = models.TextChoices(choices=TypeUser.choices,default=TypeUser.TYPE_FREE)
