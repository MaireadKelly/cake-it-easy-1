from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    related_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="subcategories")

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} -> {self.name}"
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    preview_description = models.CharField(max_length=255)  # Use TextField if it's longer
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    image = CloudinaryField("image", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Cake(models.Model):
    OCCASION_CHOICES = [
        ("wedding", "Wedding"),
        ("birthday", "Birthday"),
        ("anniversary", "Anniversary"),
        ("baby_shower", "Baby Shower"),
        ("gender_reveal", "Gender Reveal"),
        ("Communion", "Communion"),
        ("Confirmation", "Confirmation"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField("image", blank=True, null=True)  # Use CloudinaryField to store images
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(
        max_length=50, choices=OCCASION_CHOICES, default="other"
    )

    def __str__(self):
        return self.name
