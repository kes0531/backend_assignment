# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import Profile
from .serializers import UserSerializer

from django.contrib.auth import authenticate

class UserProfileAPI(APIView) :
    def get(self, request, userid):
        user_data = Profile.objects.filter(userid=userid)
        serializer = UserSerializer(user_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserSignupAPI(APIView) :
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class UserLoginAPI(APIView) :
    def post(self, request):
        serializer = UserSerializer(data=request.data)
