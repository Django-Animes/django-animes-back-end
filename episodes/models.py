from django.db import models

class Episode(models.Model):
    name = models.TextField(default='')
    video_hd_url = models.TextField(default='')
    video_sd_url = models.TextField(default='')
    anime = models.ForeignKey('animes.Anime',on_delete=models.CASCADE,related_name='episodes')

