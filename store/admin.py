from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http.request import HttpRequest
from .models import *
# Register your models here.

@admin.register(Category)
class CateogryAdmin(admin.ModelAdmin):
    list_display=['title','product_count']
    search_fields=['title']
    
    def product_count(self,category):
        return category.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','category']
    list_editable=['price']
    list_filter=['category']
    search_fields=['name','price','category']
    autocomplete_fields=['category']
    
    list_per_page=10
    
    def stock(self,product):
        if product.inventory>10:
            return 'In Stock'
        elif product.inventory<10:
            return 'Low Stock'
    
admin.site.register(Customer)


class OrerItemInline(admin.TabularInline):
    model=OrderItem
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrerItemInline]