from django.db import models
from common.models import CommonModel

class Review(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product=models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order_detail = models.ForeignKey('order_details.OrderDetail', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    rating_choice = ((1,1),(2,2),(3,3),(4,4),(5,5))
    rating = models.PositiveIntegerField(choices=rating_choice)
    best = models.BooleanField(default=False,blank=True,null=False)  
    