from django.db import models


class ExternalGame(models.Model):
    external_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    thumbnail = models.URLField(blank=True)
    short_description = models.TextField(blank=True)
    game_url = models.URLField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    platform = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=150, blank=True)
    developer = models.CharField(max_length=150, blank=True)
    release_date = models.DateField(blank=True, null=True)
    freetogame_profile_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title