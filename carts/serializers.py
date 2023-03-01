from rest_framework import serializers
from .models import Cart
from products.serializers import OrderDetailProductSerializer

class CartsSerializer(serializers.ModelSerializer):
    product = OrderDetailProductSerializer()
    class Meta:
        model = Cart
        fields = ('id','product','count','options')