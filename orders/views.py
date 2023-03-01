from django.shortcuts import render
from rest_framework.views    import APIView
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import exceptions, decorators, permissions
from rest_framework import status
from order_details.serializers import OrderDetailSerializer



class OrderView(APIView):
    
    def post(self, request):
               
        try:
            order_serializer = OrderSerializer(data=request.data['order'])            
            order_serializer.is_valid(raise_exception=True)
            order_serializer.save()
            print(order_serializer.data['id'])
            
            for detail in request.data['details']:
                detail['order'] = order_serializer.data['id']
                detail_serializer = OrderDetailSerializer(data=detail)
                detail_serializer.is_valid(raise_exception=True)
                detail_serializer.save()
            
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        except:
                      
            return Response(detail_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        