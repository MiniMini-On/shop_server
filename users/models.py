from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

class User(AbstractUser):
    uid = models.CharField(max_length=150, editable=False, unique=True)
    username = models.CharField(max_length=50, unique=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, null=True)
    grade = models.ForeignKey('user_grades.UserGrade', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.uid
   
