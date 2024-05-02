from django.urls import path
from playlists.views import index, music, singer

urlpatterns = [
    path("", index, name="home-page"),
    path("musics/", music, name="musics-page"),
    path("singers/", singer, name="singers-page"),
]
