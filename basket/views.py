from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Cake
from .models import Basket, BasketItem


# Add to basket view
def add_to_basket(request, cake_id):
    """Add a quantity of the specified product to the basket"""
    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = int(request.POST.get('quantity', 1))

    # Retrieve session key for the basket
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    # Retrieve or create a basket
    basket, _ = Basket.objects.get_or_create(session_key=session_key)
    basket_item, created = BasketItem.objects.get_or_create(basket=basket, cake=cake)

    if not created:
        basket_item.quantity += quantity  # Increase the quantity if item already exists
    else:
        basket_item.quantity = quantity

    basket_item.save()
    messages.success(request, f'Added {cake.name} to your basket.')

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

