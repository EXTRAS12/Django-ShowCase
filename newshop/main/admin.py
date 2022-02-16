from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    """Добавление категорий в админке"""
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    """Добавление товара в админке"""
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated', 'image']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    actions = ['delete_selected']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
