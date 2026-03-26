from django.contrib import admin
from .models import Genre, Platform, Game


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "producer", "status", "release_date", "created_at")
    list_filter = ("status", "genre", "platforms")
    search_fields = ("title", "description", "producer")