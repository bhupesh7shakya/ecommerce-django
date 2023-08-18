from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Category,Product,Cart
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from . import serializers
from django.db.models import Count
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from . import permissions as pd
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
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


class CartViewset(generics.CreateAPIView,generics.ListAPIView):
   # serializer_class=serializers.CartSerializer
   # queryset=Cart.objects.prefetch_related('cart_items__product').all()
   permission_classes=[permissions.IsAuthenticated]
   
   
   def get_queryset(self):
       return Cart.objects\
          .prefetch_related('cart_items')\
          .filter(user=self.request.user)
          
   
   
   def get_serializer_class(self):
      if self.request.method=="POST":
         return serializers.CreateCartSerializer
      
      return serializers.CartSerializer
   
