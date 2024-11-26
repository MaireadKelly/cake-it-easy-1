# basket/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket, BasketItem
from products.models import Cake


def add_to_basket(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    customer = request.user.customer if request.user.is_authenticated else None
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    basket, created = Basket.objects.get_or_create(
        customer=customer, session_key=session_key
    )
    item, created = BasketItem.objects.get_or_create(basket=basket, cake=cake)
    if not created:
        item.quantity += 1  # Increase the quantity if the item already exists
    item.save()

    return redirect("view_basket")


def remove_from_basket(request, item_id):
    """Remove an item from the basket"""
    try:
        item = get_object_or_404(BasketItem, id=item_id)
        item.delete()
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)


def view_basket(request):
    customer = None
    if request.user.is_authenticated:
        # Automatically create the customer profile if it doesn't exist
        customer, created = Customer.objects.get_or_create(user=request.user)

    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    # Retrieve or create a basket based on the customer and session key
    basket = Basket.objects.filter(customer=customer, session_key=session_key).first()

    # Passing basket items to the template in the same format as the walkthrough
    basket_items = basket.items.all() if basket else []

    total = sum(item.quantity * item.cake.price for item in basket_items)
    grand_total = total  # You can add delivery costs if needed

    context = {
        "basket_items": basket_items,
        "total": total,
        "grand_total": grand_total,
        "free_delivery_delta": max(
            0, 50 - total
        ),  # Example: Assuming free delivery above 50 euros
    }

    return render(request, "basket/basket.html", context)


def update_basket(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id)
    if request.method == "POST":
        new_quantity = int(request.POST.get("quantity", 1))
        item.quantity = new_quantity
        item.save()

    return redirect("view_basket")
