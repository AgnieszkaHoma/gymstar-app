from django.test import TestCase, Client
from django.urls import reverse
from store.models import Product
import json

class TestViews(TestCase):    
    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')
           
    def test_products_GET(self):
        response = self.client.get(self.products_url)      
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/products.html')