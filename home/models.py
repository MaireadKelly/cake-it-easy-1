from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from home.customer import Customer # Import Customer from New customer.py file

class Order(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="orders", default=1) 
    customer = models.ForeignKey("home.Customer", on_delete=models.CASCADE, blank=True, null=True, related_name="orders")
    quantity = models.PositiveIntegerField()
    inscription = models.CharField(max_length=255, default="No inscription")
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
            ("pending", "Pending"),
            ("shipped", "Shipped"),
            ("delivered", "Delivered"),
        ],
        default="pending",
    )
    delivery_time = models.DateTimeField()
    delivery_address = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order of {self.product.name} (x{self.quantity})"

class Comment(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="comments", default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.customer.user.username} on {self.product.name}"

class Rating(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True, null=True, related_name="ratings")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="ratings", default=1)
    rating = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Rating {self.rating} by {self.customer.user.username} for {self.product.name}"
