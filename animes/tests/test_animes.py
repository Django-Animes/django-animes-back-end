import ipdb
from django.test import Client,TestCase

class AnimesTest(TestCase):
    
    BASE_URL = "/api/animes/"

    @classmethod
    def setUpTestData(cls):
        cls.anime_data = {
            "name"  : "Naruto",
            "image_url" : "naruto.png",
            "release_date" : "2001",
            "description" : "Pode ser um pouco duro as vezes",
            "genres" : [{"name" : "Shounen"}]
        }
    def test_creation_of_anime(self):
        api = Client()
        anime_creation_response = api.post(path=self.BASE_URL,data=self.anime_data)
        ipdb.set_trace()

        


