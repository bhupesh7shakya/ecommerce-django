from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from . import serializers
# Create your views here.

@api_view(['GET','POST'])
def category_list(request):
    if request.method=='GET':
        cateogory=Category.objects.all()
        serializer=serializers.CateogrySerializer(cateogory,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=serializers.CateogrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail":"data saved succesfully"
        },status=status.HTTP_201_CREATED)
    
    
    

@api_view(['GET','PUT','DELETE'])
def category_detail(request,id):
    category=get_object_or_404(Category,id=id)
    serializer=serializers.CateogrySerializer(category)
    if request.method=='PUT':
        serializer=serializers.CateogrySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        return Response("PUT REQUEST")

    elif request.method=='DELETE':
        
        product_count=Product.objects.filter(category=id).count()
        if product_count >0:
               return Response({'detail':'Category cannot be deleted because it alot products' },
            status=status.HTTP_200_OK
        )
        category.delete()
        return Response({'detail':'deleted successfully' },
            status=status.HTTP_200_OK
        )

    return Response(serializer.data)
    
    

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
