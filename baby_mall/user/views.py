from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework import mixins, generics

from .models import Profile
from .serializers import UserSerializer

from django.contrib.auth import authenticate

# mixin 사용 전 코드
# class UserProfileAPI(APIView) :
#     def get(self, request, userid):
#         user_data = Profile.objects.filter(userid=userid)
#         serializer = UserSerializer(user_data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class UserProfileAPI(mixins.RetrieveModelMixin, generics.GenericAPIView) : 
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'userid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) # profile 정보 가져오기

class UserProfileEditAPI(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'userid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) # profile 수정하기


class UserSignupAPI(APIView) :
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(): # 유효한 값이라면
            serializer.save() # DB 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class UserLoginAPI(APIView) :
    def get(self, request):
        return Response()
