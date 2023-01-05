from django.db import models

class Achievement(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    type_of_achievement = models.CharField(max_length=255)
        
        
"""  through="achievements.Achievement_user", """      
        
""" 
class Achievement_user(models.Model):  
        achievament_id: models.ForeignKey(
            "achievements.Achievement",
            on_delete=models.CASCADE,
        )
        user_id: models.ForeignKey(
            "users.User",
            on_delete=models.CASCADE,
        )
        created_at = models.DateField(auto_now=True) """