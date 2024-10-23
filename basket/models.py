from django.db import models
from home.models import Cake, Customer


# Create your models here.
class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="baskets", null=True, blank=True)
    session_key = models.CharField(max_length=255, null=True, blank=True
    )  # For guest checkout
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Basket for {self.customer.user.username if self.customer else 'Guest'}"

    @property
    def total_price(self):
        return sum(
            item.total_price for item in self.items.all()
        )  # Calculate total price of basket items


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="items")
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.cake.price
