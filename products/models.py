from django.db import models
from common.models import CommonModel



# Create your models here.
class Product(CommonModel):
    name = models.CharField(max_length=30)
    category = models.ForeignKey('product_categories.ProductCategory', on_delete=models.CASCADE)  
    theme = models.ForeignKey('themes.Theme', on_delete=models.SET_NULL, null=True)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)
    option = models.ForeignKey('product_options.ProductOption',on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    desc = models.TextField(max_length=1000, blank=True, null=True)
    hits = models.PositiveIntegerField(default=0)
    image1=models.CharField(max_length=255, blank=True, null=True)
    image2=models.CharField(max_length=255, blank=True, null=True)
    like= models.PositiveIntegerField(default=0, blank=True, null=False)