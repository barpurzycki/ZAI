from django.contrib import admin
from .models import ExternalGame


@admin.register(ExternalGame)
class ExternalGameAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "platform", "publisher", "release_date")
    search_fields = ("title", "genre", "publisher", "developer")
    list_filter = ("genre", "platform", "publisher")