from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('categories',views.category_list),
    path('categories/<id>',views.category_detail),
    path('products',views.product_list),
    path('products/<id>',views.product_detail)
]