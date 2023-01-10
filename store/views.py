from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.db.models import Q


# Create your views here.
def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def category_list(request, slug=None):
    category = get_object_or_404(Category, slug=slug)   
    products = Product.objects.filter(category=category, is_available=True).order_by('-published_at')
    
    context = {
        'category': category,
        'products': products,
    }
    
    return render(request, 'store/category-search.html', context)


def allProducts(request):
    product_page = Product.objects.filter(is_available=True).order_by('-published_at')
    categories = Category.objects.all()
    price_filter = Price_Filter.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    size = Size.objects.all()
     
    # p = Paginator(Product.objects.filter(is_available=True).order_by('-published_at'), 15) 
    # page = request.GET.get('page')
    # product_page = p.get_page(page)
    # nums = "c" * product_page.paginator.num_pages
         
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
        product_page = Product.objects.filter(category=CategoryID)
    elif PriceFilterID:
        product_page = Product.objects.filter(price_filter=PriceFilterID)
    elif BrandID:
        product_page = Product.objects.filter(brand=BrandID)    
    elif SizeID:
        product_page = Product.objects.filter(size=SizeID)   
    elif ColorID:
        product_page = Product.objects.filter(color=ColorID)
    elif LOWTOHIGHID:
        product_page = Product.objects.filter().order_by('price')
    elif HIGHTOLOWID:
        product_page = Product.objects.filter().order_by('-price')
    elif ATOZID:
        product_page = Product.objects.filter().order_by('name')
    elif ZTOAID:
        product_page = Product.objects.filter().order_by('-name')
    else:
        product_page = Product.objects.filter(is_available=True)
        
    context = {
        'categories': categories,
        'price_filter': price_filter,
        'color': color, 
        'size': size,
        'brand': brand,
        'product_page': product_page,
        # 'nums': nums,
    }
    return render(request, 'store/products.html', context)


def productInfo(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.visits = product.visits + 1
    product.recent_visits = datetime.now()
    product.save()
    
    if request.method == 'POST' and request.user.is_authenticated:
        points = request.POST.get('points', 1)
        body = request.POST.get('body', '')
        review = Review.objects.create(product=product, user=request.user, points=points, body=body).order_by('-created_at')
        return redirect('productInfo', slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'store/productInfo.html', context)

class Search(ListView):
    model = Product
    template_name = 'store/search.html'
    context_object_name = 'searchedProduct'

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if not query :
            query = "error"
            
        return Product.objects.filter(name__icontains=query).order_by('-published_at')

