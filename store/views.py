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
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class CategoryViewset(ModelViewSet):
   queryset=Category.objects.all()
   serializer_class = serializers.CateogrySerializer


    
class ProductViewset(ModelViewSet):
    queryset=Product.objects.select_related('category').all()
    serializer_class=serializers.ProductSerializer
    filter_backends =(DjangoFilterBackend,SearchFilter,OrderingFilter)
    filterset_class  = ProductFilter
    search_fields =['name',]
    ordering_fields=['price']
    pagination_class=PageNumberPagination
