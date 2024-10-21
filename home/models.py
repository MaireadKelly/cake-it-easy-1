from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class Cake(models.Model):
    OCCASION_CHOICES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('anniversary', 'Anniversary'),
        ('baby_shower', 'Baby Shower'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="cakes/")
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50, choices=OCCASION_CHOICES, default='other')
    available_stock = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            for i in range(1, 100):
                if not Cake.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{slugify(self.name)}-{i}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)  # Capital 'C' here
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, null=True, related_name="orders")
    quantity = models.PositiveIntegerField()
    inscription = models.CharField(max_length=255, default='No inscription')
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending')
    delivery_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.price = self.cake.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order of {self.cake.name} (x{self.quantity})"


class Customer(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def previous_orders(self):
        return self.order_set.all()
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(default=1)  # A scale of 1 to 5
