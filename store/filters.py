from django_filters import FilterSet
from . import models

class ProductFilter(FilterSet):
    class Meta:
        model = models.Product
        fields = {
            'category_id':['exact'], 
            'price':['gt','lt']
        }