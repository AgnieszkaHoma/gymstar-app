from store.models import Product
from decimal import Decimal

class Wishlist():
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get('session-key')
        
        if 'session-key' not in request.session:
            wishlist = self.session['session-key'] = {}
        
        self.wishlist = wishlist
        
    def add(self, product, prod_qty):
        product_id = str(product.id)
        
        if product_id in self.wishlist:
            self.wishlist[product_id]['qty'] = prod_qty
        else:
            self.wishlist[product_id] = {'price': str(product.price), 'qty': prod_qty}  
        
        self.session.modified = True
        
    def __len__(self):
        return sum(item['qty'] for item in self.wishlist.values())
    
    def __iter__(self):
        all_item_ids = self.wishlist.keys()
        products = Product.objects.filter(id__in=all_item_ids)
        wishlist = self.wishlist.copy()
        
        for product in products:
            wishlist[str(product.id)]['product'] = product
            
        for item in wishlist.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            
            yield item

            
    def delete(self, product):
        product_id = str(product)
        
        if product_id in self.wishlist:
            del self.wishlist[product_id]
                   
        self.session.modified = True
        
        