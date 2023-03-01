from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  
    list_display = ("name","category", "theme", "artist",)
    list_filter = ("category","theme", "artist", "hits",)
    ordering = ("category",)
    search_fields = ("name","category", "theme", "artist",)
