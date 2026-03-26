from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Game(models.Model):
    class Status(models.TextChoices):
        PLANOWANA = "planowana", "Planowana"
        DOSTEPNA = "dostepna", "Dostępna"
        UKONCZONA = "ukonczona", "Ukończona"

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="games",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    producer = models.CharField(max_length=150, blank=True)
    release_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DOSTEPNA,
    )
    platforms = models.ManyToManyField(
        Platform,
        blank=True,
        related_name="games",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]
        constraints = [
            models.UniqueConstraint(
                fields=["genre", "title"],
                name="uniq_game_title_in_genre"
            )
        ]

    def __str__(self):
        return self.title