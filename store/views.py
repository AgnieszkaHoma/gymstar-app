from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from datetime import datetime


# Create your views here.
def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def category_list(request, slug=None):
    category = get_object_or_404(Category, slug=slug)   
     
    products = Product.objects.filter(category=category)
    
    context = {
        'category': category,
        'products': products,
    }
    
    return render(request, 'store/category-search.html', context)


def allProducts(request):
    products = Product.objects.filter(is_available=True).order_by('-published_at')
    categories = Category.objects.all()
    price_filter = Price_Filter.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()
        
    ColorID = request.GET.get('colorID')
    CategoryID = request.GET.get('category')
    PriceFilterID = request.GET.get('price_filter') 
    BrandID = request.GET.get('brandID') 
    SizeID = request.GET.get('sizeID')
      
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    LOWTOHIGHID = request.GET.get('LOWTOHIGH')
    HIGHTOLOWID = request.GET.get('HIGHTOLOW')
    
    if CategoryID:
        products = Product.objects.filter(category=CategoryID)
    elif PriceFilterID:
        products = Product.objects.filter(price_filter=PriceFilterID)
    elif BrandID:
        products = Product.objects.filter(brand=BrandID)    
    elif SizeID:
        products = Product.objects.filter(size=SizeID)   
    elif ColorID:
        products = Product.objects.filter(color=ColorID)
    elif LOWTOHIGHID:
        products = Product.objects.filter().order_by('price')
    elif HIGHTOLOWID:
        products = Product.objects.filter().order_by('-price')
    elif ATOZID:
        products = Product.objects.filter().order_by('name')
    elif ZTOAID:
        products = Product.objects.filter().order_by('-name')
    else:
        products = Product.objects.filter(is_available=True)
        
    context = {
        'products': products,
        'categories': categories,
        'price_filter': price_filter,
        'color': color, 
        'size': size,
        'brand': brand,
    }
    return render(request, 'store/products.html', context)


def productInfo(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.visits = product.visits + 1
    product.recent_visits = datetime.now()
    product.save()
    
    context = {
        'product': product
    }
    return render(request, 'store/productInfo.html', context)

class Search(ListView):
    model = Product
    template_name = 'store/search.html'
    context_object_name = 'searchedProduct'

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if not query :
            query = ""
            
        return Product.objects.filter(name__icontains=query).order_by('-published_at')

