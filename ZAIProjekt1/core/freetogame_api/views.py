from datetime import date
import requests

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExternalGame
from .serializers import ExternalGameSerializer


class ExternalGameViewSet(viewsets.ModelViewSet):
    queryset = ExternalGame.objects.all()
    serializer_class = ExternalGameSerializer
    filterset_fields = ["genre", "platform", "publisher", "developer"]
    search_fields = ["title", "genre", "publisher", "developer"]
    ordering_fields = ["title", "release_date", "created_at"]
    ordering = ["title"]


@api_view(["POST"])
def import_games(request):
    url = "https://www.freetogame.com/api/games"

    params = {}
    platform = request.data.get("platform")
    category = request.data.get("category")
    sort_by = request.data.get("sort_by")

    if platform:
        params["platform"] = platform
    if category:
        params["category"] = category
    if sort_by:
        params["sort-by"] = sort_by

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()

    created_count = 0
    updated_count = 0

    for item in data:
        release_date = None
        if item.get("release_date"):
            try:
                release_date = date.fromisoformat(item["release_date"])
            except ValueError:
                release_date = None

        obj, created = ExternalGame.objects.update_or_create(
            external_id=item["id"],
            defaults={
                "title": item.get("title", ""),
                "thumbnail": item.get("thumbnail", ""),
                "short_description": item.get("short_description", ""),
                "game_url": item.get("game_url", ""),
                "genre": item.get("genre", ""),
                "platform": item.get("platform", ""),
                "publisher": item.get("publisher", ""),
                "developer": item.get("developer", ""),
                "release_date": release_date,
                "freetogame_profile_url": item.get("freetogame_profile_url", ""),
            },
        )

        if created:
            created_count += 1
        else:
            updated_count += 1

    return Response(
        {
            "message": "Import completed",
            "created": created_count,
            "updated": updated_count,
            "total_in_db": ExternalGame.objects.count(),
        },
        status=status.HTTP_200_OK,
    )