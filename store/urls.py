from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.allProducts, name='products'),
    path('products/<slug:slug>/', views.productInfo, name='productInfo'),
    path('category-search/<slug:slug>/', views.category_list, name='category_list'),
    path('search/', views.Search.as_view(), name='search'),
]