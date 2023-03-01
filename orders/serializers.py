from rest_framework import serializers
from .models import Order
from users.serializers import UserIdSerializer


        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'