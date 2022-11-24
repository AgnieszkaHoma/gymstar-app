from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404


# Create your views here.

def allProducts(request):
    products = Product.objects.filter(is_product_available=True).order_by('-published_at')
    categories = Category.objects.all()
        
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/products.html', context)


def productInfo(request, slug):
    product = Product.objects.get(slug=slug)
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

