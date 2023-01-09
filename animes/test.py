import ipdb
from rest_framework.test import APITestCase,APIClient
from rest_framework.views import status
from users.models import User

class AnimesTest(APITestCase):
    
    BASE_URL = "/api/animes/"
    LOGIN_URL = "/api/user/login/"

    @classmethod
    def setUpTestData(cls):
        cls.anime_data = {
            "name"  : "Naruto",
            "image_url" : "naruto.png",
            "release_date" : "2001",
            "description" : "Pode ser um pouco duro as vezes",
        }
        cls.episode_data = {
            "name"  : "Naruto episodio 1",
            "video_hd_url" : "naruto em hd",
            "video_sd_url" : "naruto em sd",
        }
        cls.genre_data = {
            "name" : "Shounen"
        }

        admin_data = {"username" : "Artorys","email" : "Artorys@gmail.com","password" : "12345"}
        user_common_data = {"username" : "John", "email" : "John@gmail.com", "password" :"12345"}
        
        User.objects.create_user(**user_common_data)
        User.objects.create_superuser(**admin_data)

        cls.api_without_token = APIClient()

        login_adm = cls.api_without_token.post(path=cls.LOGIN_URL,data=admin_data)
        login_common_user = cls.api_without_token.post(path=cls.LOGIN_URL,data=user_common_data)

        token_adm = login_adm.json()["access"]
        token_common_user = login_common_user.json()["access"]


        cls.api = APIClient()
        cls.api.credentials(HTTP_AUTHORIZATION='Bearer ' + token_adm)
        
        cls.api_common_user = APIClient()
        cls.api_common_user.credentials(HTTP_AUTHORIZATION='Bearer ' + token_common_user)

        creation_anime = cls.api.post(path=cls.BASE_URL,data=cls.anime_data)
        creation_episode = cls.api.post(path=cls.BASE_URL + "episode/",data=cls.episode_data)
        creation_genre = cls.api.post(path=cls.BASE_URL + "genre/",data=cls.genre_data)

        cls.anime_id = creation_anime.json()["id"]
        cls.episode_id = creation_episode.json()["id"]
        cls.genre_id = creation_genre.json()["id"]

    def test_creation_of_anime(self):
        response = self.api.post(path=self.BASE_URL,data=self.anime_data)
        self.assertIs(status.HTTP_201_CREATED,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
        self.assertIn("image_url",response.json())
        self.assertIn("release_date",response.json())
        self.assertIn("description",response.json())
        self.assertIn("genres",response.json())
        self.assertIn("episodes",response.json())

    def test_creation_of_episode(self):
        response = self.api.post(self.BASE_URL + "episode/",self.episode_data)
        self.assertIs(status.HTTP_201_CREATED,response.status_code)
        self.assertIn("name",response.json())
        self.assertIn("video_hd_url",response.json())
        self.assertIn("video_sd_url",response.json())

    def test_creation_of_genre(self):
        response = self.api.post(self.BASE_URL + "genre/",self.genre_data)
        self.assertIs(status.HTTP_201_CREATED,response.status_code)
        self.assertIn("name",response.json())
    
    def test_add_episode_in_anime(self):
        episode_id  = {"episode_id" : self.episode_id}
        response = self.api.post(self.BASE_URL + f"{self.anime_id}/episode/",data=episode_id)
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("episodes",response.json())
        episodes = response.json()["episodes"]
        self.assertIs(len(episodes),1)
    
    def test_add_genre_in_anime(self):
        genre_id = {"genre_id" : self.genre_id}
        response = self.api.post(self.BASE_URL + f"{self.anime_id}/genre/",data=genre_id)
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("genres",response.json())
        genres = response.json()["genres"]
        self.assertIs(len(genres),1)

    def test_list_anime(self):
        response = self.api.get(self.BASE_URL)
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("results",response.json())
        self.assertIsInstance(response.json()["results"],list)
        self.assertIn("id",response.json()["results"][0])
        self.assertIn("name",response.json()["results"][0])
        self.assertIn("image_url",response.json()["results"][0])
        self.assertIn("release_date",response.json()["results"][0])
        self.assertIn("description",response.json()["results"][0])
        self.assertIn("amount_of_episodes",response.json()["results"][0])
        self.assertIn("episodes",response.json()["results"][0])
        self.assertIn("genres",response.json()["results"][0])
    
    def test_list_anime_hd(self):
        response = self.api.get(self.BASE_URL  + "hd/")
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("results",response.json())

    def test_list_episode(self):
        response = self.api.get(self.BASE_URL + "episode/")
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("results",response.json())
        self.assertIsInstance(response.json()["results"],list)
        self.assertIn("id",response.json()["results"][0])
        self.assertIn("name",response.json()["results"][0])
        self.assertIn("video_hd_url",response.json()["results"][0])
        self.assertIn("video_sd_url",response.json()["results"][0])

    def test_list_genre(self):
        response = self.api.get(self.BASE_URL + "genre/")
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("results",response.json())
        self.assertIsInstance(response.json()["results"],list)
        self.assertIn("id",response.json()["results"][0])
        self.assertIn("name",response.json()["results"][0])
    
    def test_retrieve_anime(self):
        response = self.api.get(self.BASE_URL + f"{self.anime_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
        self.assertIn("image_url",response.json())
        self.assertIn("release_date",response.json())
        self.assertIn("description",response.json())
        self.assertIn("genres",response.json())
        self.assertIn("episodes",response.json())

    def test_retrieve_episode(self):
        response = self.api.get(self.BASE_URL + f"episode/{self.episode_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
        self.assertIn("video_hd_url",response.json())
        self.assertIn("video_sd_url",response.json())

    def test_retrieve_genre(self):
        response = self.api.get(self.BASE_URL + f"genre/{self.genre_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
    
    def test_edit_anime(self):
        anime_edit = {"name" : "Naruto Shippuden","description" : "Naruto mais velho"}
        response = self.api.patch(self.BASE_URL + f"{self.anime_id}/",data=anime_edit)
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
        self.assertEqual(anime_edit["name"],response.json()["name"])
        self.assertIn("description",response.json())
        self.assertEqual(anime_edit["description"],response.json()["description"])
    
    def test_edit_episode(self):
        episode_edit = {"name" : "Naruto Shippuden ep 1"}
        response = self.api.patch(self.BASE_URL + f"episode/{self.episode_id}/",data=episode_edit)
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
        self.assertEqual(episode_edit["name"],response.json()["name"])

    def test_edit_episode_inside_anime(self):
        episode_id  = {"episode_id" : self.episode_id}
        response = self.api.post(self.BASE_URL + f"{self.anime_id}/episode/",data=episode_id)
        episode_edit = {"episode_id": {self.episode_id},"name" : "Boruto"}
        response = self.api.patch(self.BASE_URL + f"{self.anime_id}/episode/",data=episode_edit)
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
        self.assertEqual(episode_edit["name"],response.json()["name"])

    def test_edit_genre(self):
        genre_edit = {"name" : "Drama"}
        response = self.api.patch(self.BASE_URL + f"genre/{self.genre_id}/",data=genre_edit)
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
        self.assertEqual(genre_edit["name"],response.json()["name"])
        
    def test_edit_genre_inside_anime(self): 
        genre_id = {"genre_id" : self.genre_id}
        response = self.api.post(self.BASE_URL + f"{self.anime_id}/genre/",data=genre_id)
        genre_edit = {"genre_id": {self.genre_id},"name" : "Action"}
        response = self.api.patch(self.BASE_URL + f"{self.anime_id}/genre/",data=genre_edit)
        self.assertIs(status.HTTP_200_OK,response.status_code)
        self.assertIn("id",response.json())
        self.assertIn("name",response.json())
        self.assertEqual(genre_edit["name"],response.json()["name"])
    
    def test_delete_anime(self):
        response = self.api.delete(self.BASE_URL + f"{self.anime_id}/")
        self.assertIs(status.HTTP_204_NO_CONTENT,response.status_code)

    def test_delete_episode(self):
        response = self.api.delete(self.BASE_URL + f"episode/{self.episode_id}/")
        self.assertIs(status.HTTP_204_NO_CONTENT,response.status_code)

    def test_delete_episode_inside_anime(self):
        episode_id  = {"episode_id" : self.episode_id}
        response = self.api.post(self.BASE_URL + f"{self.anime_id}/episode/",data=episode_id)
        response = self.api.delete(self.BASE_URL + f"{self.anime_id}/episode/",data=episode_id)
        self.assertIs(status.HTTP_204_NO_CONTENT,response.status_code)
    
    def test_delete_genre(self):
        response = self.api.delete(self.BASE_URL + f"genre/{self.genre_id}/")
        self.assertIs(status.HTTP_204_NO_CONTENT,response.status_code)

    def test_delete_genre_inside_anime(self):
        genre_id  = {"genre_id" : self.genre_id}
        response = self.api.post(self.BASE_URL + f"{self.anime_id}/genre/",data=genre_id)
        response = self.api.delete(self.BASE_URL + f"{self.anime_id}/genre/",data=genre_id)
        self.assertIs(status.HTTP_204_NO_CONTENT,response.status_code)

    def test_creation_anime_without_token(self):
        response = self.api_without_token.post(path=self.BASE_URL,data=self.anime_data)
        self.assertIs(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_creation_anime_using_user_common_token(self):
        response = self.api_common_user.post(path=self.BASE_URL,data=self.anime_data)
        self.assertIs(status.HTTP_403_FORBIDDEN,response.status_code)

    def test_creation_episode_without_token(self):
        response = self.api_without_token.post(path=self.BASE_URL + "episode/",data=self.episode_data)
        self.assertIs(status.HTTP_401_UNAUTHORIZED,response.status_code)
    
    def test_creation_episode_using_user_common_token(self):
        response = self.api_common_user.post(path=self.BASE_URL  + "episode/",data=self.episode_data)
        self.assertIs(status.HTTP_403_FORBIDDEN,response.status_code)

    def test_creation_genre_without_token(self):
        response = self.api_without_token.post(path=self.BASE_URL + "genre/",data=self.genre_data)
        self.assertIs(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_add_episode_in_anime_without_token(self):
        episode_id = {"episode_id" : self.episode_id}
        response = self.api_without_token.post(path=self.BASE_URL + f"{self.anime_id}/episode/",data=episode_id)
        self.assertIs(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_add_episode_in_anime_using_user_common_token(self):
        episode_id = {"episode_id" : self.episode_id}
        response = self.api_common_user.post(path=self.BASE_URL + f"{self.anime_id}/episode/",data=episode_id)
        self.assertIs(status.HTTP_403_FORBIDDEN,response.status_code)
    
    def test_add_genre_in_anime_without_token(self):
        genre_id = {"genre_id" : self.genre_id}
        response = self.api_without_token.post(path=self.BASE_URL + f"{self.anime_id}/genre/",data=genre_id)
        self.assertIs(status.HTTP_401_UNAUTHORIZED,response.status_code)
    
    def test_add_genre_in_anime_using_user_common_token(self):
        genre_id = {"genre_id" : self.genre_id}
        response = self.api_common_user.post(path=self.BASE_URL + f"{self.genre_id}/episode/",data=genre_id)
        self.assertIs(status.HTTP_403_FORBIDDEN,response.status_code)
    
    def test_list_anime_without_token(self):
        response = self.api_without_token.get(path=self.BASE_URL)
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_list_anime_using_user_common_token(self):
        response = self.api_common_user.get(path=self.BASE_URL)
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_list_episode_without_token(self):
        response = self.api_without_token.get(path=self.BASE_URL + "episode/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_list_episode_using_user_common_token(self):
        response = self.api_common_user.get(path=self.BASE_URL + "episode/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_list_genre_without_token(self):
        response = self.api_without_token.get(path=self.BASE_URL + "genre/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_list_genre_using_user_common_token(self):
        response = self.api_common_user.get(path=self.BASE_URL + "genre/")
        self.assertIs(status.HTTP_200_OK,response.status_code)
    
    def test_retrieve_anime_without_token(self):
        response = self.api_without_token.get(path=self.BASE_URL + f"{self.anime_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_retrieve_anime_using_user_common_token(self):
        response = self.api_common_user.get(path=self.BASE_URL + f"{self.anime_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_retrieve_episode_without_token(self):
        response = self.api_without_token.get(path=self.BASE_URL + f"episode/{self.episode_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_retrieve_episode_using_user_common_token(self):
        response = self.api_common_user.get(path=self.BASE_URL + f"episode/{self.episode_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_retrieve_genre_without_token(self):
        response = self.api_without_token.get(path=self.BASE_URL + f"genre/{self.genre_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_retrieve_genre_using_user_common_token(self):
        response = self.api_common_user.get(path=self.BASE_URL + f"genre/{self.genre_id}/")
        self.assertIs(status.HTTP_200_OK,response.status_code)

    def test_edit_anime_without_token(self):
        response = self.api_without_token.patch(path=self.BASE_URL + f"{self.anime_id}/")
        self.assertIs(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_edit_anime_using_user_common_token(self):
       response = self.api_common_user.patch(path=self.BASE_URL + f"{self.anime_id}/")
       self.assertIs(status.HTTP_403_FORBIDDEN,response.status_code)

    def test_edit_episode_without_token(self):
        response = self.api_without_token.patch(path=self.BASE_URL + f"episode/{self.episode_id}/")
        self.assertIs(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_edit_episode_using_user_common_token(self):
        response = self.api_common_user.patch(path=self.BASE_URL + f"episode/{self.episode_id}/")
        self.assertIs(status.HTTP_403_FORBIDDEN,response.status_code)

    def test_edit_genre_without_token(self):
        response = self.api_without_token.patch(path=self.BASE_URL + f"genre/{self.genre_id}/")
        self.assertIs(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_edit_genre_using_user_common_token(self):
        response = self.api_common_user.patch(path=self.BASE_URL + f"genre/{self.genre_id}/")
        self.assertIs(status.HTTP_403_FORBIDDEN,response.status_code)

    
    
    

        


