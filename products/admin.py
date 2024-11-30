from django.contrib import admin
from .models import Category, Product, Cake, CakeSize, CustomCake

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
    filter_horizontal = ('sizes',)  # Add this line for the sizes field

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'description',)

@admin.register(CakeSize)
class CakeSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)

@admin.register(CustomCake)
class CustomCakeAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'filling', 'inscription', 'price', 'image',)
    prepopulated_fields = {"slug": ("flavor", "filling",)}
    filter_horizontal = ('sizes',)  # Add this line for the sizes field
