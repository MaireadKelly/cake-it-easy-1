# home/customer.py
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)  # Street address
    address_line2 = models.CharField(max_length=255, blank=True, null=True)  # Optional second line
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)  # Changed from state to county
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - Customer Profile"

    @property
    def previous_orders(self):
        return self.orders.all()  # Assuming related_name='orders' in the Order model
