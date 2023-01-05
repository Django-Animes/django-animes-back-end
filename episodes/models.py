from django.db import models

class Episode(models.Model):
    name = models.TextField()
    video_hd_url = models.TextField()
    video_sd_url = models.TextField()
    anime = models.ForeignKey('animes.Anime',on_delete=models.CASCADE,related_name='episodes')
