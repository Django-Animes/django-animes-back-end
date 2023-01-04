from django.db import models

class Anime(models.Model):
    name = models.TextField(default='')
    image_url = models.TextField(default='')
    release_date = models.TextField(default='')
    description = models.TextField(default='')
    amount_of_episodes = models.IntegerField(default=0)
    genres = models.ManyToManyField('genres.Genre',related_name='animes')

