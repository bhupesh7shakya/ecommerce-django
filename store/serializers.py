# from decimal import Decimal
from decimal import Decimal
from rest_framework import serializers
from . import models
class CateogrySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)
    
class ProductSerializer(serializers.Serializer):
    
    # class Meta:
    #     model=models.Product
    #     fields=['name','inventory','price',]
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=255)
    inventory=serializers.IntegerField()
    category=serializers.StringRelatedField()
    price=serializers.FloatField()
    price_with_tax=serializers.SerializerMethodField('taxed_price')
    
    def taxed_price(self,product):
        return product.price+(product.price*Decimal(0.13))