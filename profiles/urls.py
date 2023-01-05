from django.urls import path
from .views import ProfileListCreate, ProfileUpdateDelete

urlpatterns = [
    path("user/profile/", ProfileListCreate.as_view()),
    path("user/profile/", ProfileUpdateDelete.as_view()),
]
