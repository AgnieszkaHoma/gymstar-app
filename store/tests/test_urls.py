from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import *

class TestUrls(SimpleTestCase):   
    def test_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, allProducts)
    def test_productinfo_url_is_resolved(self):
        url = reverse('productInfo', args=[3])
        self.assertEquals(resolve(url).func, productInfo)