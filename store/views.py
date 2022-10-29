from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

def allProducts(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store/products.html', context)

def productInfo(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'store/productInfo.html', context)