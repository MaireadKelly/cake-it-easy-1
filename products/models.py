from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# ---- CATEGORY MODEL ----
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="subcategories"
    )

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} -> {self.name}"
        return self.name

# ---- BASE PRODUCT MODEL ----
class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("cake", "Cake"),
        ("custom_cake", "Custom Cake"),
        ("cupcake", "Cupcake"),
        ("accessory", "Accessory"),
    ]

    name = models.CharField(max_length=255, unique=True)
    product_type = models.CharField(
        max_length=50, choices=PRODUCT_TYPE_CHOICES, default="cake"
    )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, related_name="products", null=True, blank=True
    )
    image = CloudinaryField("image", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        """Automatically generate a unique slug if not provided."""
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            # Ensure slug uniqueness
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# ---- STANDARD CAKE MODEL ----
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
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    toppers_allowed = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.occasion})"

# ---- CUSTOMIZATION MODELS ----
class Flavour(models.Model):
    """ Cake and Cupcake flavours """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Flavours"

    def __str__(self):
        return self.name

class Filling(models.Model):
    """ Fillings for custom cakes """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Frosting(models.Model):
    """ Frosting/Icing options for custom cakes """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CakeSize(models.Model):
    """ Cake size options for custom cakes """
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size

# ---- CUSTOM CAKE MODEL ----
class CustomCake(Product):
    flavour = models.ForeignKey(Flavour, on_delete=models.SET_NULL, null=True)
    filling = models.ForeignKey(Filling, on_delete=models.SET_NULL, null=True)
    frosting = models.ForeignKey(Frosting, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(CakeSize, on_delete=models.SET_NULL, null=True, blank=True)
    custom_message = models.BooleanField(default=False)
    inscription = models.CharField(max_length=255, blank=True, null=True)
    toppers = models.JSONField(default=list, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Custom Cake - {self.flavour.name if self.flavour else 'No Flavour'} with {self.filling.name if self.filling else 'No Filling'}"

# ---- CUPCAKE MODEL ----
class Cupcake(Product):
    flavour = models.ForeignKey(Flavour, on_delete=models.SET_NULL, null=True)
    frosting = models.ForeignKey(Frosting, on_delete=models.SET_NULL, null=True)
    custom_message = models.BooleanField(default=False)

    def __str__(self):
        return f"Custom Cupcake - {self.flavour.name if self.flavour else 'No Flavour'}"

# ---- ACCESSORY MODEL ----
class Accessory(Product):
    ACCESSORY_TYPE_CHOICES = [
        ("candles", "Candles"),
        ("toppers", "Cake Toppers"),
        ("banners", "Banners"),
        ("balloons", "Balloons"),
    ]

    accessory_type = models.CharField(
        max_length=50, choices=ACCESSORY_TYPE_CHOICES, default="candles"
    )

    class Meta:
        verbose_name_plural = "Accessories"

    def __str__(self):
        return f"{self.name} ({self.accessory_type})"
