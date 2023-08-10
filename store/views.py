from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from . import serializers
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.




class CategoryViewset(ModelViewSet):
   queryset=Category.objects.all()
   serializer_class = serializers.CateogrySerializer


    

@api_view(['GET'])
def product_list(request):
    products = Product.objects.select_related('category').all()
    serializer=serializers.ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request,id):
    product=get_object_or_404(Product,id=id)
    serializer=serializers.ProductSerializer(product)
    return Response(serializer.data)
