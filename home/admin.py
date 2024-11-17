from django.contrib import admin
from .models import Product, Order, Customer, Comment, Rating

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'slug', 'category')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'status', 'delivery_time')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'email')

admin.site.register(Comment)
admin.site.register(Rating)
