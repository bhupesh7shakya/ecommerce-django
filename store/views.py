from django.shortcuts import render
from .models import Category,Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import serializers
# Create your views here.

@api_view(['GET'])
def category_list(request):
    cateogory=Category.objects.all()
    serializer=serializers.CateogrySerializer(cateogory,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.select_related('category').all()
    serializer=serializers.ProductSerializer(products,many=True)
    return Response(serializer.data)