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


# def add(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             products = int(request.POST.get('product_id'))
#             product_check = Product.objects.get(id=products)
#             cart_id = int(request.POST.get('cart_id'))
#             cart_check = Cart.objects.get_or_create(id = cart_id)
#             if (product_check):
#                 if (OrderItem.objects.filter(user = request.user.id, product_id=products, cart_i = cart_id)):
#                     return JsonResponse({'status': "Product Already in Cart"})
#                 else:
#                     prod_qty = int(request.POST.get('quantity'))
#                     cart_id = request.POST.get('cart')
                    
#                     if product_check.quantity >= prod_qty and cart_check is not None : 
#                         OrderItem.objects.create(user= request.user, product_id=products, product_qty = prod_qty, cart = cart_id, cartitems=cart_check)
#                         return JsonResponse({'status': "Product added successfully"})
#                     else:
#                         return JsonResponse({'status': "Only" + str(product_check.quantity) +" quantity available"})
#             else:
#                 return JsonResponse({'status': "No such product found"})
#         else:
#             return JsonResponse({'status': "Login to continue"})
#     return render(request, 'cart/cart.html')