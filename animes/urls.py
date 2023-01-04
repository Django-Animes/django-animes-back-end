from django.urls import path
from animes.views import AnimesView

urlpatterns = [
    path('animes/',AnimesView.as_view()),
]