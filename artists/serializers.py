from rest_framework import serializers
from .models import Artist


class ProductArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('nickname',)