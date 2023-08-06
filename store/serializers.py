from rest_framework import serializers
from . import models
class CateogrySerializer(serializers.Serializer):
    title=serializers.CharField(max_length=255)
    
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Product
        fields=['name','inventory','price',]
    # name=serializers.CharField(max_length=255)
    # description=serializers.TextField()