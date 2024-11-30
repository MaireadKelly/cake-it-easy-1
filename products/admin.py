from django.contrib import admin
from .models import Category, Product, Cake, CakeSize, CustomCake


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'slug', 'category', 'product_type')
    list_filter = ('product_type', 'category',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'occasion', 'price', 'image', 'get_sizes')
    list_filter = ('occasion', 'category')
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name', 'category',)
    filter_horizontal = ('sizes',)  # For ManyToManyField sizes

    # Custom method to display sizes in list view
    def get_sizes(self, obj):
        return ", ".join([size.get_name_display() for size in obj.sizes.all()])
    get_sizes.short_description = "Sizes"


@admin.register(CustomCake)
class CustomCakeAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'filling', 'inscription', 'price', 'image', 'get_sizes')
    list_filter = ('flavor', 'filling')
    prepopulated_fields = {"slug": ("flavor", "filling")}
    filter_horizontal = ('sizes',)  # For ManyToManyField sizes

    # Custom method to display sizes in list view
    def get_sizes(self, obj):
        return ", ".join([size.get_name_display() for size in obj.sizes.all()])
    get_sizes.short_description = "Sizes"


@admin.register(CakeSize)
class CakeSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'description')
    list_filter = ('parent',)
