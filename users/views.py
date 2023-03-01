from django.shortcuts import render
from . import serializers
import requests
from .models import User
# from django.contrib.auth import login as auth_login, logout as auth_logout
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework import exceptions, decorators, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from django.conf import settings
from django.utils import timezone




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
def login(user, request):

    tokens = get_tokens_for_user(user)
    res = Response()
    serializer = serializers.UserSerializer(user)

    res.data = tokens
    res.set_cookie(
        key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
        value=tokens["refresh"],
        expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
        # secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
        # httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
        # samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
    )
    res.data['username'] = serializer.data['username']
   
    res.headers["X-CSRFToken"] = csrf.get_token(request)
    
    
    return res




class KaKaoSignInCallBackView(APIView):
    def post(self, request):
        serializer = serializers.KakaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auth_code = serializer.validated_data["code"]
        # auth_code = request.GET.get('code')
        kakao_token_api = 'https://kauth.kakao.com/oauth/token'
        data = {
            'grant_type': 'authorization_code',
            'client_id': '9c2ae003d16074d931b7184aef49825a',
            'redirection_uri': 'http://localhost:3000/oauth/callback/kakao',
            'code': auth_code
        }

        token_response = requests.post(kakao_token_api, data=data)

        access_token = token_response.json().get('access_token')

        user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'})
        print(user_info_response.json())
        kakao_id = user_info_response.json()['id']
        # kakao_nick = user_info_response.json()['properties']['nickname']
        kakao_age = user_info_response.json()['kakao_account']['age_range']
        kakao_birthday = user_info_response.json()['kakao_account']['birthday']
        kakao_gender = user_info_response.json()['kakao_account']['gender']
        print(kakao_id)
        try:
            user = User.objects.get(uid='1'+str(kakao_id))
            print(user)
            user.last_login = timezone.now()
            user.save()
            # auth_login(request,user)
            print('login')
            
            return login(user, request)
            
        except User.DoesNotExist:
            # 기존에 가입된 유저가 없으면 새로 가입
            random_nick = requests.get('https://nickname.hwanmoo.kr/?format=json&count=1')
            new_user = User(uid = '1'+str(kakao_id), username=random_nick.json()['words'][0],age=kakao_age, birthday=kakao_birthday, gender=kakao_gender)
            new_user.save()
            print('register')
            user = User.objects.get(uid='1'+str(kakao_id))
            # auth_login(request,user)
            return login(user, request)
    
    
@decorators.permission_classes([permissions.IsAuthenticated])
class UserInfoView(APIView) :
    
    def get(self, request):
        try: 
            user = User.objects.get(id=request.user.id)
            serializer = serializers.UserSerializer(user)
            print(serializer.data)
            if serializer.data['uid'][0] == 1:
                serializer.data.social = 'kakao'
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response('유효한 유저가 아닙니다.')
        
@decorators.permission_classes([permissions.IsAuthenticated])
class UserRegisterView(APIView):
    def post(self, request):
        try:
            user = User.objects.get(id=request.user.id)
            serializer = serializers.UserSerializer(user, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=200)
        except User.DoesNotExist:
            return Response("등록되지 않은 사용자입니다.")
        
@decorators.permission_classes([permissions.IsAuthenticated])

class LogoutView(APIView):
    def post(self, request):
        try:
            refreshToken = request.COOKIES.get('refresh')
            token = RefreshToken(refreshToken)
            token.blacklist()
            res = Response()
            # res.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
            # res.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
            res.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
            # res.delete_cookie("X-CSRFToken")
            # res.delete_cookie("csrftoken")
            res["X-CSRFToken"]=None
            # auth_logout(request)
            res.data = {'msg':"logout"}
                        
            return res
        except:
            raise exceptions.ParseError("Invalid token")
        

            
            
        

            