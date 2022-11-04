from django.db import models
from django.urls import reverse 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    
    def get_absolute_url(self):
      return reverse('categoriesTypes', args=[self.slug])
   
    def __str__(self):
      return self.name 
    
class Product(models.Model):
    name = models.CharField(max_length=100) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    slug = models.SlugField(max_length=250, unique=True)
    stock = models.IntegerField()
    is_product_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/product_image')
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    published_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
        
    class Meta:
       ordering = ('-published_at',)
       
    def get_absolute_url(self):
       return reverse('productInfo', args=[self.slug])
       
    def __str__(self):
      return self.name
    