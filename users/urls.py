from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("user/register/", views.UserView.as_view()),
    path("user/<int:pk>/", views.UserDetailView.as_view()),
    path("users/", views.UserListView.as_view()),
    path("user/login/", jwt_views.TokenObtainPairView.as_view()),
    path("user/achievements/<int:user_id>/", views.AchievementUpdateView.as_view()),
]
"""   path("user/", views.UserDetailView.as_view()), """