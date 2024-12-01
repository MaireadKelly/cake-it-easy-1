from django.contrib import admin
from .models import Category, Product, Cake, CustomCake


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "product_type", "price", "category", "image", "slug")
    list_filter = ("product_type", "category")
    prepopulated_fields = {"slug": ("name",)}
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "parent")


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ("name", "occasion", "price", "category", "image", "slug")
    list_filter = ("occasion", "category",)  # Use a tuple for single field
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CustomCake)
class CustomCakeAdmin(admin.ModelAdmin):
    list_display = (
        "flavor",
        "filling",
        "inscription",
        "price",
        "image",
        "slug",
    )
    list_filter = ("flavor", "filling")
    prepopulated_fields = {"slug": ("flavor", "filling")}


# @admin.register(Accessory)
# class AccessoryAdmin(admin.ModelAdmin):
#     list_display = ("name", "accessory_type", "price", "category", "image", "slug")
#     list_filter = ("accessory_type", "category")
#     prepopulated_fields = {"slug": ("name",)}
