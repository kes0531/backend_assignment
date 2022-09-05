from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductAPI(APIView) :
    def get(self, request, pid):
        product_data = Product.objects.filter(pid=pid)
        serializer = ProductSerializer(product_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductAllAPI(APIView) :
    def get(self, request):
        product_data = Product.objects.all()
        serializer = ProductSerializer(product_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductSignupAPI(APIView) :
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  