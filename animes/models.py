from django.db import models

class Anime(models.Model):
    name = models.TextField(unique=True)
    image_url = models.TextField()
    release_date = models.TextField()
    description = models.TextField()
    amount_of_episodes = models.IntegerField(default=0)
    genres = models.ManyToManyField('genres.Genre',related_name='animes')

