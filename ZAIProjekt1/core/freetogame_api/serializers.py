from rest_framework import serializers
from .models import ExternalGame


class ExternalGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalGame
        fields = "__all__"