from django.db import models

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey('profile.Profile', on_delete=models.CASCADE, related_name='comments')
    anime = models.ForeignKey('animes.Anime',on_delete=models.CASCADE,related_name='episodes')
    likes = models.BigIntegerField(default=0)
