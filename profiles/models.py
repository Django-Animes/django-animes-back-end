from django.db import models


class Episodes_viewed(models.Model):
    profile = models.ForeignKey(
        "profiles.Profile", on_delete=models.CASCADE, related_name="viewed_profile"
    )
    episode = models.ForeignKey(
        "episodes.Episode", on_delete=models.CASCADE, related_name="viewed_episode"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    name = models.CharField(max_length=40)
    avatar_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_episode_viewed = models.TextField(default="")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="profiles"
    )
    episodes_viewed = models.ManyToManyField(
        "episodes.Episode",
        related_name="profiles_viewed",
        through="profiles.Episodes_viewed",
    )
    animes = models.ManyToManyField("animes.Anime", related_name="profiles")
