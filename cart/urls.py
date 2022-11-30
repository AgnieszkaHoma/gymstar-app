from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart', views.add, name='add'),

]