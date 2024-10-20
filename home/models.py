from django.db import models


# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="cakes/")

    def __str__(self):
        return self.name


class Order(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.cake.name} (x{self.quantity})"


class Customer(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
