from django.shortcuts import render
from .models import Cart
from rest_framework.views    import APIView
from rest_framework.response import Response
from . import serializers



class CartsView(APIView):
    def get(self, request,user_id):
        cart = Cart.objects.filter(user_id=user_id)
        serializer = serializers.CartsSerializer(cart, many=True)
        return Response(serializer.data)
