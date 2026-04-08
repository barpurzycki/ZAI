from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExternalGameViewSet, import_games

router = DefaultRouter()
router.register("games", ExternalGameViewSet, basename="externalgame")

urlpatterns = [
    path("", include(router.urls)),
    path("import/", import_games, name="import_games"),
]