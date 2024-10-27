from django.contrib import admin
from .models import Cake, Order, Customer, Comment, Rating

# Register your models here.
@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category','image', 'price')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'cake', 'quantity', 'status', 'delivery_time')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'email')

admin.site.register(Comment)
admin.site.register(Rating)