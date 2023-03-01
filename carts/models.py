from django.db import models
from common.models import CommonModel



# Create your models here.
class Cart(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)  
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)  
    count=models.PositiveIntegerField(default=1,blank=True,null=False)
    options = models.CharField(max_length=255)