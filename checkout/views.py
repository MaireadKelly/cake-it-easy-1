import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import models
from .models import Order, OrderLineItem, CustomCake
from basket.models import Basket, BasketItem
from products.models import Cake
from .forms import OrderForm


# Create your views here.


from django.contrib import messages


def checkout(request):
    basket = Basket.objects.filter(session_key=request.session.session_key).first()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            # Create order line items from the basket
            if basket:
                for item in basket.items.all():
                    line_item = OrderLineItem(
                        order=order,
                        cake=item.cake,
                        quantity=item.quantity,
                        lineitem_total=item.cake.price * item.quantity,
                    )
                    line_item.save()

            # Clear the basket after saving the order
            basket.items.all().delete()
            messages.success(request, "Your order has been placed successfully!")

            return redirect("order_confirmation", order_number=order.order_number)
        else:
            messages.error(
                request, "There was an error with your form. Please check your details."
            )
            return redirect("checkout")  # Redirect back to checkout in case of an error
    else:
        form = OrderForm()

    return render(request, "checkout/checkout.html", {"form": form, "basket": basket})


def order_confirmation(request, order_number):
    """View to handle order confirmation"""
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, "checkout/order_confirmation.html", {"order": order})
