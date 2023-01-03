from django.db import models
from accounts.models import User
from decimal import Decimal
from store.models import Product

# Create your models here.

class Discount(models.Model):
    code = models.CharField(max_length=20)
    amount = models.FloatField()
    
    def __str__(self):
        return self.code
    
# class Payment(models.Model):
#     STATUS = (
#     ('In process', 'In process'),
#     ('Success', 'Success'),
#     ('Rejected', 'Rejected'),
#     )    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     payment_id = models.CharField(max_length=100)
#     method = models.CharField(max_length=50)
#     price_to_paid = models.CharField(max_length=100)
#     status = models.CharField(choices=STATUS, max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.payment_id
    
# class Order(models.Model):
#     STATUS = (
#         ('New', 'New'),
#         ('Accepted for execution', 'Accepted for execution'),
#         ('Completed', 'Completed'),
#         ('Sent', 'Sent'),
#         ('Cancelled', 'Cancelled'),
#     )

#     date_started = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
#     order_number = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     country = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     street = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     order_note = models.CharField(max_length=100, blank=True)
#     order_total = models.FloatField()
#     discount = models.FloatField()
#     status = models.CharField(max_length=100, choices=STATUS, default='New')
#     ip = models.CharField(blank=True, max_length=20)
#     is_ordered = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'

#     def full_address(self):
#         return f'{self.street} {self.state} {self.country}'

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'