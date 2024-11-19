from django.contrib import admin
from .models import Category, Product, Cake

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'slug', 'category', 'product_type')
    list_filter = ('product_type', 'category',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Cake)   
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'occasion', 'price', 'image',)
    list_filter = ('occasion', 'category',)
    prepopulated_fields = {"slug": ("name",)}
        
    ordering = ('name', 'category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'description',)