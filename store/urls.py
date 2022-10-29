from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.allProducts, name='products'),
    path('products/<slug:slug>/', views.productInfo, name='productInfo'),
]