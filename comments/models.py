from django.db import models


class Comment(models.Model):
    class Meta:
        ordering = ("id",)

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.BigIntegerField(default=0)

    # profile = models.ForeignKey(
    #     "profile.Profile",
    #     on_delete=models.CASCADE,
    #     related_name="comments",
    # )
    episode = models.ForeignKey(
        "episodes.Episode",
        on_delete=models.CASCADE,
        related_name="comments",
    )
