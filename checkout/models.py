from django.db import models
from home.models import Cakke, Customer
from basket.models import Basket

# Create your models here.

class Order(models.Model):
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending')
    ordered_at = models.DateTimeField(auto_now_add=True)    #
    delivery_time = models.DateTimeField(auto_now_add=True)
    

def __str__(self):
    return f"Order {self.id} for {self.customer.user.username}"
