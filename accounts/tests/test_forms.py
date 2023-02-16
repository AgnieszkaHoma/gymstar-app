from django.test import SimpleTestCase
from accounts.forms import ShippingForm

class TestForms(SimpleTestCase):
    
    def test_shipping_form_valid_data(self):
        form = ShippingForm(data={
            'name' : 'Agnieszka',
            'surname' : 'Homa', 
            'email': 'agnieszka.homa@gmail.com',
            'street': 'Błekitna 15',
            'country': 'Poland',
            'state': 'Podkarpackie',
            'city': 'Rzeszów',
            'pin_code': '12-345',
            
        })
        
        self.assertTrue(form.is_valid())
        
    def test_shipping_form_no_data(self):
        form = ShippingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        
        
        