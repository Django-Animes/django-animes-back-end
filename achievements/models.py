from django.db import models
from users.models import User


class Achievement(models.Model):
        name = models.CharField(max_length=255)
        url = models.CharField(max_length=255)
        type_of_achievement = models.CharField(max_length=255)
        users = models.ManyToManyField(
            "users.User",
            through="achievements.userProfile",
            related_name="achievements",
        )

class Achievement_user(models.Model):  
        achievament_id: models.ForeignKey(
            Achievement,
            on_delete=models.CASCADE,
        )
        user_id: models.ForeignKey(
            User,
            on_delete=models.CASCADE,
        )
        created_at = models.DateField(auto_now=True)