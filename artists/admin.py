from django.contrib import admin

# Register your models here.
from .models import Artist

# Register your models here.

@admin.register(Artist)
class ArtistsAdmin(admin.ModelAdmin):  
    pass
    
