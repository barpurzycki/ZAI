from django.urls import path
from .views import (
    GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView,
    GenreListView, GenreDetailView, GenreCreateView, GenreUpdateView, GenreDeleteView
)

urlpatterns = [
    path("", GameListView.as_view(), name="game_list"),
    path("game/<int:pk>/", GameDetailView.as_view(), name="game_detail"),
    path("game/add/", GameCreateView.as_view(), name="game_add"),
    path("game/<int:pk>/edit/", GameUpdateView.as_view(), name="game_edit"),
    path("game/<int:pk>/delete/", GameDeleteView.as_view(), name="game_delete"),

    path("genres/", GenreListView.as_view(), name="genre_list"),
    path("genre/<int:pk>/", GenreDetailView.as_view(), name="genre_detail"),
    path("genre/add/", GenreCreateView.as_view(), name="genre_add"),
    path("genre/<int:pk>/edit/", GenreUpdateView.as_view(), name="genre_edit"),
    path("genre/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre_delete"),
]