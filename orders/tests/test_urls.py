from django.test import SimpleTestCase
from django.urls import reverse, resolve
from orders.views import *

class TestUrls(SimpleTestCase):
    def test_checkout_url_is_working(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)    
    def test_paymentsuccess_url_is_working(self):
        url = reverse('payment_success')
        self.assertEquals(resolve(url).func, payment_success)    
    def test_paymentfailed_url_is_working(self):
        url = reverse('payment_failed')
        self.assertEquals(resolve(url).func, payment_failed)   