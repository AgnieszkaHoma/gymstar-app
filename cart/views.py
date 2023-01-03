from django.shortcuts import render, redirect
from accounts import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from accounts import *
from store.models import Product
from .models import *
from django.http import JsonResponse
from .utils import Cart

# Create your views here.

def cart(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart.html', context)

def add_to_cart(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id')) #drugi product_id jest z ajaxa
        prod_quantity = int(request.POST.get('prod_quantity'))
        
        product = get_object_or_404(Product, id = product_id)
        
        cart.add(product=product, prod_qty = prod_quantity)
        
        cart_amount_qty = cart.__len__()
        
        response = JsonResponse({'qty': cart_amount_qty })
        return response

def remove_from_cart(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id')) 
        
        cart.delete(product=product_id)
        
        cart_amount_qty = cart.__len__()
        
        cart_total_amount = cart.total_amount()
        
        response = JsonResponse({'qty': cart_amount_qty, 'total_am': cart_total_amount})
        
        return response

def update_cart(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id')) 
        prod_quantity = int(request.POST.get('prod_quantity'))
        
        cart.update(product=product_id, qty = prod_quantity)
        
        cart_amount_qty = cart.__len__()
        
        cart_total_amount = cart.total_amount()
        
        response = JsonResponse({'qty': cart_amount_qty, 'total_am': cart_total_amount})
        
        return response
