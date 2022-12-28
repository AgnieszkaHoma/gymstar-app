from django.db import models
from django.urls import reverse 
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    
    class Meta:
      verbose_name_plural = 'Categories'
      
    def __str__(self):
      return self.name 
  
    def get_absolute_url(self):
      return reverse('category_list', args=[self.slug])
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
      return self.name   
    
class Size(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
      return self.name    
    
class Color(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    
    def __str__(self):
      return self.name  
class Price_Filter(models.Model):
    PRICE_FILTER = (
      ('0 to 50', '0 to 50'),
      ('50 to 100', '50 to 100'),
      ('100 to 150', '100 to 150'),
      ('150 to 200', '150 to 200'),
      ('200 to 250', '200 to 250'),
      ('250 to 500', '250 to 500'),
    )
    price = models.CharField(choices=PRICE_FILTER, max_length=50)
    
    def __str__(self):
      return self.price  
      
class Product(models.Model):

    
    name = models.CharField(max_length=100) 
    category = models.ForeignKey(Category, related_name= 'product',on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    price_filter = models.ForeignKey(Price_Filter, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    slug = models.SlugField(max_length=250, unique=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/product_image')
    description = RichTextField(blank=True, null=True)
    visits = models.IntegerField(default=0)
    recent_visits = models.DateTimeField(null=True, blank = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    published_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
        
    class Meta:
       ordering = ('-published_at',)
       
    def get_absolute_url(self):
       return reverse('productInfo', args=[self.slug])
       
    def __str__(self):
      return self.name 
    
    def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super(Product, self).save(*args, **kwargs)
