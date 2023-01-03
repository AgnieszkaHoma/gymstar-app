from django.urls import path
from . import views

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('paymentFailed', views.payment_failed, name='payment_failed'),
    path('paymentSuccess', views.payment_success, name='payment_success'),
    path('finish_order', views.finish_order, name='finish_order'),
]