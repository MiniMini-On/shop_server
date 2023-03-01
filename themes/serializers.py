from rest_framework import serializers
from .models import Theme


class ProductThemeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Theme
        fields = ('name',)