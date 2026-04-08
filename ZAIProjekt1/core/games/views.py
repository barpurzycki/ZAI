from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game, Genre
from .forms import GameForm, GenreForm


class GameListView(ListView):
    model = Game
    template_name = "games/game_list.html"
    context_object_name = "games"


class GameDetailView(DetailView):
    model = Game
    template_name = "games/game_detail.html"
    context_object_name = "game"


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = "games/game_form.html"
    success_url = reverse_lazy("game_list")


class GameUpdateView(UpdateView):
    model = Game
    form_class = GameForm
    template_name = "games/game_form.html"
    success_url = reverse_lazy("game_list")


class GameDeleteView(DeleteView):
    model = Game
    template_name = "games/game_confirm_delete.html"
    success_url = reverse_lazy("game_list")


class GenreListView(ListView):
    model = Genre
    template_name = "games/genre_list.html"
    context_object_name = "genres"


class GenreDetailView(DetailView):
    model = Genre
    template_name = "games/genre_detail.html"
    context_object_name = "genre"


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = "games/genre_form.html"
    success_url = reverse_lazy("genre_list")


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "games/genre_form.html"
    success_url = reverse_lazy("genre_list")


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = "games/genre_confirm_delete.html"
    success_url = reverse_lazy("genre_list")