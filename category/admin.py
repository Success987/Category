from django.contrib import admin
from category.models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail')
    search_fields = ('name__startswith', 'name__endswith', )
    fields = ('name', 'image', )
    list_filter = ('created_at',)


