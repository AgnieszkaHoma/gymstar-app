from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.filter(is_available=True).order_by('-published_at')
    popular = Product.objects.all().order_by('-visits')[0:4]
    last_viewed = Product.objects.all().order_by('-recent_visits')[0:4]
    
    context = {
        'products': products,
        'popular':popular,
        'last_viewed': last_viewed
    }
    
    return render(request, 'home.html', context)