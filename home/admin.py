from django.contrib import admin
from .models import Cake, Order, Customer, Comment, Rating

# Register your models here.
admin.site.register(Cake)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Comment)
admin.site.register(Rating)