from django import forms
from .models import *
from orders.models import *

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        
    def clean(self):
        cleaned_data = super(RegisterUserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
      
class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['name', 'surname', 'email', 'street', 'country', 'state', 'city', 'pin_code']
        