from django.shortcuts import render, redirect
from django.db import models
from basket.models import Basket, BasketItem

# Create your views here.

def checkout(request):
    customer = request.user.customer
    basket = Basket.objects.filter(customer=customer).first()
    
    if request.method == 'POST':
        delivery_time = request.POST.get('delivery_time')
        order = Order.objects.create(
            customer=customer,
            basket=basket,
            delivery_time=delivery_time
            )
        basket.delete() # Clear the basket after order is placed
        return redirect('order_confirmation', {'basket': basket})
