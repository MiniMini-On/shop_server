from django.contrib import admin
from .models import ProductOption
# Register your models here.

@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):  
    list_display = ("category","option1", "option2", "option3",)
    list_filter = ("category","option1", "option2", "option3",)
    ordering = ("category",)
    search_fields = ("category",)
    
