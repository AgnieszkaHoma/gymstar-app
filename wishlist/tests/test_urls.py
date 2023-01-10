from django.test import SimpleTestCase
from django.urls import reverse, resolve
from wishlist.views import *

class TestUrls(SimpleTestCase):
    
    def test_wishlist_url_is_resolved(self):
        url = reverse('wishlist')
        self.assertEquals(resolve(url).func, wishlist)