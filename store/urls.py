from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('categories',views.CategoryViewset.as_view()),
    path('categories/<pk>',views.CategoryViewset.as_view({'get':'list','post':'create','put':'update','delete':'delete'})),
    path('products',views.product_list),
    path('products/<id>',views.product_detail)
]