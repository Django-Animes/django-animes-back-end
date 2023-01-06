from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("achievements/", views.AchievementView.as_view()),
    path("achievements/<int:pk>/",views.AchievementRetrieveUpdateDestroy.as_view()),
    path("achievements/user/<int:pk>/",views.AchievementUserCreate.as_view())
]
