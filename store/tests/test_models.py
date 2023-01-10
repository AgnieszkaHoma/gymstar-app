from django.test import TestCase
from store.models import *

class TestModels(TestCase):
    
    def test_size_model(self):
        name = Size.objects.create(name='S')
        self.assertEqual(str(name), 'S')
    def test_brand_model(self):
        name = Size.objects.create(name='Nike')
        self.assertEqual(str(name), 'Nike')