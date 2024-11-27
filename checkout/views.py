from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.db import models
from .models import Order, OrderLineItem
from basket.models import Basket
from products.models import Cake
from .forms import OrderForm
import stripe

# Create your views here.

def checkout(request):
    """
    Handles the checkout process, including order creation and payment.
    """
    # Get the basket from the session
    basket = request.session.get("basket", {})
    if not basket:
        messages.error(request, "Your basket is empty, please add items before proceeding to checkout.")
        return redirect('products')
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.customer = request.user.customer  # Assign customer if logged in
            order.save()

            # Create order line items from the basket
            for cake_id, item_data in basket.items():
                cake = get_object_or_404(Cake, pk=cake_id)
                line_item = OrderLineItem(
                    order=order,
                    cake=cake,
                    quantity=item_data.get("quantity", 1),
                    cake_size=item_data.get("size"),
                )
                line_item.save()

            # Clear the basket after saving the order
            request.session["basket"] = {}
            messages.success(request, "Your order has been placed successfully!")
            return redirect("order_confirmation", order_number=order.order_number)
        else:
            messages.error(request, "There was an error with your form. Please check your details and try again.")
    else:
        form = OrderForm()

    return render(request, "checkout/checkout.html", {"form": form})

def order_confirmation(request, order_number):
    """
    Displays the order confirmation page.
    """
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, "checkout/order_confirmation.html", {"order": order})
