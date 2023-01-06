from .utils import Wishlist

def context_wishlist(request):
    return {'wishlist': Wishlist(request)}