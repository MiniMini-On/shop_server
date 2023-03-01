from django.db import models

# Create your models here.
class ProductOption(models.Model):
    option1 = models.CharField(max_length=200, blank=True, null=True)
    option2 = models.CharField(max_length=200, blank=True, null=True)
    option3 = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey('product_categories.ProductCategory', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'[{self.option1}],[{self.option2}],[{self.option3}]'