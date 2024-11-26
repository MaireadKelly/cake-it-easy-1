from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Cake
from .models import Basket, BasketItem


# Add to basket view
def add_to_basket(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    quantity = int(request.POST.get('quantity', 1))  # Get quantity from the form
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    basket, created = Basket.objects.get_or_create(session_key=session_key)
    item, created = BasketItem.objects.get_or_create(basket=basket, cake=cake)
    if not created:
        item.quantity += quantity  # Increase the quantity if the item already exists
    else:
        item.quantity = quantity  # Set initial quantity
    item.save()

    return redirect('view_basket')


# View basket contents
def view_basket(request):
    """A view that renders the basket contents page"""
    session_key = request.session.session_key
    basket = Basket.objects.filter(session_key=session_key).first()

    return render(request, 'basket/basket.html', {'basket': basket})


# Update the quantity of an item in the basket
def update_basket(request, item_id):
    """Adjust the quantity of the specified product in the basket"""
    item = get_object_or_404(BasketItem, id=item_id)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        if new_quantity > 0:
            item.quantity = new_quantity
            item.save()
            messages.success(request, f'Updated {item.cake.name} quantity to {item.quantity}.')
        else:
            item.delete()
            messages.success(request, f'Removed {item.cake.name} from your basket.')

    return redirect('view_basket')

