from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Cake, CustomCake, Cupcake, Accessory, Category, Flavour, Filling, Frosting, CakeSize

# ---- HELPER FUNCTION TO DISPLAY FOREIGN KEY IN ADMIN ----
def get_flavour(obj):
    return obj.flavour.name if obj.flavour else "No Flavour"
get_flavour.admin_order_field = 'flavour'  # Allows sorting by flavour
get_flavour.short_description = 'Flavour'  # Sets column name in admin panel

# ---- BASE PRODUCT ADMIN (For all product types) ----
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'category', 'price', 'image_preview')
    list_filter = ('product_type', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    ordering = ['product_type', 'name']

    def image_preview(self, obj):
        """Show an image preview in the admin panel."""
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px;"/>', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image"

# ---- CUSTOM CAKE ADMIN ----
@admin.register(CustomCake)
class CustomCakeAdmin(ProductAdmin):
    list_display = ('name', get_flavour, 'filling', 'price', 'image_preview')
    list_filter = ('flavour', 'filling')

# ---- CUPCAKE ADMIN ----
@admin.register(Cupcake)
class CupcakeAdmin(ProductAdmin):
    list_display = ('name', get_flavour, 'price', 'image_preview')
    list_filter = ('flavour',)

# ---- ACCESSORY ADMIN ----
@admin.register(Accessory)
class AccessoryAdmin(ProductAdmin):
    list_display = ('name', 'accessory_type', 'price', 'image_preview')
    list_filter = ('accessory_type',)

# ---- CATEGORY ADMIN ----
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'parent')
    search_fields = ('name',)
    list_filter = ('category_type', 'parent')

# ---- CUSTOMIZATION OPTIONS ADMIN ----
admin.site.register(Flavour)
admin.site.register(Filling)
admin.site.register(Frosting)
admin.site.register(CakeSize)
