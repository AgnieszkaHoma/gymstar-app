from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/settings', views.settings, name='settings'),
    path('profile/ordersHistory', views.ordersHistory, name='ordersHistory'),
    path('profile/shippingAddress', views.shippingAddress, name='shippingAddress'),
    path('profile/orderDetail/<int:id>', views.orderDetail, name='orderDetail'),
    path('profile/deleteAccount', views.deleteAccount, name='delete'),
]