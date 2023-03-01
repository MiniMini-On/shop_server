from django.db import models

# Create your models here.
class OrderDetail(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.DO_NOTHING)
    count = models.PositiveIntegerField(default=1)
    options = models.CharField(max_length=255)
    