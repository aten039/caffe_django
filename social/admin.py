from django.contrib import admin
from .models import Link

# Register your models here.

class SocialAdmin(admin.ModelAdmin): 
    readonly_fields = ('created', 'updated')
    list_display = ('key', 'name', 'url')
    

admin.site.register(Link, SocialAdmin)