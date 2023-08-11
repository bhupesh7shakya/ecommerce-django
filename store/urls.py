from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('categories',views.CategoryViewset.as_view({'get':'list','post':'create'})),
    path('categories/<pk>',views.CategoryViewset.as_view({'get':'retrive','put':'update','delete':'delete'})),
    path('products',views.ProductViewset.as_view({'get':'list','post':'create'})),
    path('products/<id>',views.ProductViewset.as_view({'get':'retrive','put':'update','delete':'delete'}))
]