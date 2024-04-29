from django.contrib import admin
from catalog.models import Product, Category

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_published', 'created_at', 'last_updated', 'owner')
    list_filter = ('category', 'is_published', 'created_at', 'last_updated')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'last_updated')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')
