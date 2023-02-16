from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import *

class TestUrls(SimpleTestCase):
    def test_register_url_is_working(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)       
    def test_login_url_is_working(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)     
    def test_ordersHistory_url_is_working(self):
        url = reverse('ordersHistory')
        self.assertEquals(resolve(url).func, ordersHistory)      
    def test_profile_url_is_working(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

