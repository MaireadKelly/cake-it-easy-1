from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="subcategories")

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} -> {self.name}"
        return self.name


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("cake", "Cake"),
    ]

    name = models.CharField(max_length=255)
    product_type = models.CharField(
        max_length=50, choices=PRODUCT_TYPE_CHOICES, default="cake"
    )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="products", null=True, blank=True
    )
    image = CloudinaryField("image", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    is_gluten_free = models.BooleanField(default=False)  # New field
    is_vegan = models.BooleanField(default=False)  # New field
    allergens = models.TextField(blank=True, null=True)  # New field
    rating = models.FloatField(default=0)  # New field
    num_reviews = models.IntegerField(default=0)  # New field

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Cake(Product):
    OCCASION_CHOICES = [
        ("wedding", "Wedding"),
        ("birthday", "Birthday"),
        ("anniversary", "Anniversary"),
        ("baby_shower", "Baby Shower"),
        ("gender_reveal", "Gender Reveal"),
        ("communion", "Communion"),
        ("confirmation", "Confirmation"),
        ("christening", "Christening"),
        ("other", "Other"),
    ]
    occasion = models.CharField(
        max_length=50, choices=OCCASION_CHOICES, default="other"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.occasion})"


class CustomCake(Product):
    FLAVOR_CHOICES = [
        ("vanilla", "Vanilla"),
        ("chocolate", "Chocolate"),
        ("red_velvet", "Red Velvet"),
        ("lemon", "Lemon"),
        ("carrot", "Carrot"),
    ]

    FILLING_CHOICES = [
        ("chocolate", "Chocolate"),
        ("buttercream", "Buttercream"),
        ("raspberry", "Raspberry"),
        ("lemon", "Lemon"),
        ("cream_cheese", "Cream Cheese"),
    ]

    flavor = models.CharField(max_length=50, choices=FLAVOR_CHOICES, default="vanilla")
    filling = models.CharField(
        max_length=50, choices=FILLING_CHOICES, default="buttercream"
    )
    inscription = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Custom Cake - {self.flavor} with {self.filling} filling"
