from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    type_of_achievement = models.CharField(max_length=255)
