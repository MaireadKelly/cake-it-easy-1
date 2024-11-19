from django.contrib import admin
from .models import Category, Product, Cake

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'slug', 'category',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Cake)   
class Cake(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'image',)
    
    ordering = ('name', 'category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)