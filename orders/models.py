from django.db import models
from phone_field import PhoneField


class Order(models.Model):
    status_choice = (('AC', 'accept'),('DE','delivery'),('CO','complete'),('CA','cancle'))
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    detailed = models.CharField(max_length=50)
    receiver_name = models.CharField(max_length=10)
    receiver_phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    status = models.CharField(default='AC',max_length=10, choices=status_choice)
    
