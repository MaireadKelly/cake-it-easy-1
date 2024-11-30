from django.contrib import admin
from .models import Order
from home.customer import Customer

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'status', 'delivery_time')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',                # The related user
        'full_name',           # Replace first_name and last_name with full_name
        'email',               # Email
        'phone_number',        # Phone number
        'street_address1',     # Street address
        'town_or_city',        # Town or city
        'county',              # County (replaces city)
        'postcode',            # Postcode
    )
    search_fields = ('user__username', 'email', 'phone_number')  # Optional, for admin search

