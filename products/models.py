from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="subcategories")

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} -> {self.name}"
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
        ("Christening", "Christening"),
        ("other", "Other"),
    ]
    occasion = models.CharField(max_length=50, choices=OCCASION_CHOICES, default="other")
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField("image", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='cakes')

    def __str__(self):
        return self.name
    
    def generate_unique_slug(self):
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 1
        while Cake.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = self.generate_unique_slug()
    super().save(*args, **kwargs)
    
    
class CustomCake(models.Model):
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
    filling = models.CharField(max_length=50, choices=FILLING_CHOICES, default="buttercream")
    inscription = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField("image", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"Custom Cake - {self.flavor} with {self.filling} filling"

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("cake", "Cake"),
        ("cupcake", "Cupcake"),
        ("other", "Other"),
    ]
 
    product_type = models.CharField(max_length=50, choices=PRODUCT_TYPE_CHOICES, default="cake")
    name = models.CharField(max_length=255)
    preview_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    image = CloudinaryField("image", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
