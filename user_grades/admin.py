from django.contrib import admin
from .models import UserGrade
# Register your models here.

@admin.register(UserGrade)
class UserGradeAdmin(admin.ModelAdmin):  
    pass