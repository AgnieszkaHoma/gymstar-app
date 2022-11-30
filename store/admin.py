from django.contrib import admin
from .models import Category, Product, Brand, Color, Price_Filter, Size
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Price_Filter)
admin.site.register(Size)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}