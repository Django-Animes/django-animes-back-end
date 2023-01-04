from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=40)
    avatar_url = models.TextField()
    last_episode_viewed = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=True, related_name="profiles")
