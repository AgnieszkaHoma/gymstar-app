from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import *
from django.contrib.auth.decorators import login_required
from cart.utils import Cart
from .models import *
from django.http import JsonResponse
# Create your views here.
def checkout(request):
    if request.user.is_authenticated: 
            try:
                shipping_address = ShippingAddress.objects.get()
                context = {'address': shipping_address}
                return render(request, 'orders/checkout.html', context)
            except:
                return render(request, 'orders/checkout.html')
                
    else:  
        return render(request, 'orders/checkout.html')

def payment_failed(request):
    return render(request, 'orders/payment-failed.html')

def payment_success(request):
    for key in list(request.session.keys()):
        if key =="session-catch":
            del request.session[key]  
    
    return render(request, 'orders/payment-success.html')

def finish_order(request):
    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        country = request.POST.get('country')
        state = request.POST.get('state')
        street = request.POST.get('street')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin_code')
        
        address = (country + "\n" + state + "\n" + street + ", " + city + ", " + pin_code)
        
        cart = Cart(request)
        
        total_amount_to_paid = cart.total_amount()
        
        if request.user.is_authenticated:
            order = Order.objects.create(name=name, surname=surname, email=email, shipping_address=address, total_to_paid=total_amount_to_paid, user=request.user)         
            order_id = order.pk         
            for item in cart:
                OrderProduct.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'], user=request.user)
        else:
            order = Order.objects.create(name=name, surname=surname, email=email, shipping_address=address, total_to_paid=total_amount_to_paid)             
            order_id = order.pk           
            for item in cart:
                OrderProduct.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'])
        
        order_success_status = True 
        response = JsonResponse({'success': order_success_status})
        return response