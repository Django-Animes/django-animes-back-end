from django.core.management.base import BaseCommand
from rest_framework.views import status,Response,Request,APIView
import httpx
import ipdb
from animes.utils import formatUrl
from animes.models import Anime
from genres.models import Genre
from episodes.models import Episode


class Command(BaseCommand):
    ANIME_API = 'https://appanimeplus.tk/play-api.php'
    ANIME_API_IMG = 'https://cdn.appanimeplus.tk/img/'
    query_id = '?cat_id=' # need id of anime
    query_name = '?search='# need name of anime
    query_episode = '?episodios=' # need episode of anime
    query_info = '?info=' # need anime id

    def handle(self, *args,**options):
        data = httpx.get(self.ANIME_API,timeout=None)
        for anime in data.json():
            id = anime['id']
            name = anime['category_name']
            image = anime['category_image']
            image_url = f'{self.ANIME_API_IMG}{image}'
            anime_info = httpx.get(f'{self.ANIME_API}{self.query_info}{id}',timeout=None).json()[0]
            genres: str = anime_info['category_genres']
            if(genres == ''):
                continue
            genres = genres.split(',')
            new_genres = []
            old_genres = []
            for genre in genres:
                if(genre == ''):
                    continue
                genre = genre.strip()
                old_genre = {'name' : genre}
                genre,_ = Genre.objects.get_or_create(name=genre)
                old_genres.append(old_genre)
                new_genres.append(genre)
            description = anime_info['category_description']
            release_date = anime_info['ano']
            data_anime = {"name" : name,"image_url" : image_url if image_url != "" else "...","release_date" : release_date if release_date != '' else "...","description" : description if description != '' else '...'}
            anime,_ = Anime.objects.get_or_create(**data_anime)
            anime.genres.set(new_genres)
            anime_episodes : list = httpx.get(f'{self.ANIME_API}{self.query_id}{id}',timeout=None).json()
            if(not anime_episodes):
                continue
            for episode in anime_episodes:
                episode_id = episode['video_id']
                name = episode['title']
                anime_episode = httpx.get(f'{self.ANIME_API}{self.query_episode}{episode_id}',timeout=None).json()[0]
                video_sd_url = anime_episode['location']
                video_hd_url = anime_episode['locationsd']
                video_sd_url = formatUrl(video_sd_url)
                video_hd_url = formatUrl(video_hd_url)
                data_episode = {"name" : name,"anime" : anime,"video_sd_url" : video_sd_url,"video_hd_url" : video_hd_url}
                Episode.objects.get_or_create(**data_episode)