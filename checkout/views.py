import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_list_or_404
from django.db import models
from .models import Order, OrderLineItem, CustomCake
from basket.models import Basket, BasketItem
from products.models import Cake
from .forms import OrderForm


# Create your views here.

def checkout(request):
    basket = request.session.get('basket', {})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            
            # Create order line items from the basket
            for item_key, item_data in basket.items():
                cake = get_object_or_404(Cake, pk=item_key.split('-')[0])
                line_item = OrderLineItem(
                    order=order,
                    cake=cake,
                    cake_size=item_data.get('size'),
                    cake_flavor=item_data.get('flavor'),
                    cake_filling=item_data.get('filling'),
                    quantity=item_data.get('quantity'),
                )
                line_item.save()

            # Clear the basket after saving the order
            request.session['basket'] = {}
            return redirect('order_confirmation', order_number=order.order_number)
    else:
        form = OrderForm()

    return render(request, 'checkout/checkout.html', {'form': form})