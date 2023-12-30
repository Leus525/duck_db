from django.contrib import admin
from .models import Items

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'type')
# Register your models here.

admin.site.register(Items, ItemsAdmin)

# teacher - admin123

