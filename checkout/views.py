from django.shortcuts import render, redirect
from .models import Order
from .basket.models import Basket
from home.models import Customer

# Create your views here.

def checkout(request):
    customer = request.user.customer
    Basket = Basket.objects.filter(customer=customer).first()
    
    if request.method == 'POST':
        delivery_time = request.POST.get('delivery_time')
        order = Order.objects.create(
            customer=customer,
            basket=basket,
            delivery_time=delivery_time
            )
        basket.delete() # Clear the basket after order is placed
        return redirect('order_confirmation', {'basket': basket})
