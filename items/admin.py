from django.contrib import admin
from .models import Items
@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

@admin.action(description="Mark selected stories as UNpublished")
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'type')
    list_filter = ['is_published']
    list_editable = ['is_published']
    list_per_page = 15
    actions = [make_published, make_unpublished]
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('items.read_item'):
            return [f.name for f in self.model._meta.fields]
        return super(ItemsAdmin, self).get_readonly_fields(
            request, obj=obj
    )
# Register your models here.

admin.site.register(Items, ItemsAdmin)

# teacher - admin123

