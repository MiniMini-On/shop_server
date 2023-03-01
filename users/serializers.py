from rest_framework import serializers
from .models import User


        
class KakaoSerializer(serializers.Serializer):
    code = serializers.CharField()  
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "uid")
        
class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
        
class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",)