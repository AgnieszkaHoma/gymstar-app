from django.shortcuts import render, get_object_or_404
from .utils import Wishlist
from store.models import Product
from django.http import JsonResponse
from cart.utils import *

# Create your views here.
def wishlist(request):
    wishlist = Wishlist(request)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'wishlist/wishlist.html', context)

def add_to_wishlist(request):
    wishlist = Wishlist(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id')) #drugi product_id jest z ajaxa
        prod_quantity = int(request.POST.get('prod_quantity'))
        
        product = get_object_or_404(Product, id = product_id)
        
        wishlist.add(product=product, prod_qty = prod_quantity)
        
        wishlist_amount_qty = wishlist.__len__()
        
        response = JsonResponse({'qty': wishlist_amount_qty })
        return response

def remove_from_wishlist(request):
    wishlist = Wishlist(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id')) 
        
        wishlist.delete(product=product_id)
        
        wishlist_amount_qty = wishlist.__len__()     
        
        response = JsonResponse({'qty': wishlist_amount_qty})
        
        return response