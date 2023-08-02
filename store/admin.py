from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','category']
    list_editable=['price']
    list_filter=['category']
    search_fields=['name']
    
    list_per_page=10
    
    def stock(self,product):
        if product.inventory>10:
            return 'In Stock'
        elif product.inventory<10:
            return 'Low Stock'
    
admin.site.register(Customer)