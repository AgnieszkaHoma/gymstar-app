from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomModelOrder(admin.ModelAdmin):
    list_display = ('id', 'total_to_paid', 'ordered_date')
    ordering = ('-ordered_date',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

admin.site.register(Order, CustomModelOrder)
admin.site.register(OrderProduct) 