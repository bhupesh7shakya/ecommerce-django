# from decimal import Decimal
from decimal import Decimal
from rest_framework import serializers
from . import models
class CateogrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields='__all__'
    
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Product
        fields=['id','name','inventory','category','price','price_with_tax']
        
    category=serializers.StringRelatedField()
    price_with_tax=serializers.SerializerMethodField('taxed_price')
    
    def taxed_price(self,product):
        return product.price+(product.price*Decimal(0.13))