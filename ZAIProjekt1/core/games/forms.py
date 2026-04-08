from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Game, Genre


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["title", "description", "producer", "release_date", "status", "genre", "platforms"]
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if "test" in title.lower():
            raise ValidationError("Tytuł nie może zawierać słowa 'test'.")
        return title


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ["name", "description"]