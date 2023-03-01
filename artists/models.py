from django.db import models
from common.models import CommonModel
from phone_field import PhoneField


class Artist(CommonModel):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True)
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nickname
    
