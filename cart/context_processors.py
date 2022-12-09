from .utils import Cart

def context_cart(request):
    return {'cart': Cart(request)}