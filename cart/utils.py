from store.models import Product
from decimal import Decimal

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session-catch')
        
        if 'session-catch' not in request.session:
            cart = self.session['session-catch'] = {}
        
        self.cart = cart
        
    def add(self, product, prod_qty):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = prod_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': prod_qty}  
        
        self.session.modified = True
        
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
    
    def __iter__(self):
        all_item_ids = self.cart.keys()
        products = Product.objects.filter(id__in=all_item_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            
            yield item
    
    def total_amount(self):
        return sum(Decimal(item['price'])* item['qty'] for item in self.cart.values())
    
