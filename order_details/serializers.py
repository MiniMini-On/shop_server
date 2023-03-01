from rest_framework import serializers
from .models import OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class ReviewOrderDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderDetail
        fields = ('options',)