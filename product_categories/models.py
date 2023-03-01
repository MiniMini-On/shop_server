from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=30)
        
    class Meta:
        verbose_name_plural = 'ProductCategories'
    def __str__(self):
        return self.name
