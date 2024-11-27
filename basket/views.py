from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Cake
from home.models import Customer

# View that renders the basket contents page
def view_basket(request):
    """ A view that renders the basket contents page """
    customer, _ = Customer.objects.get_or_create(user=request.user) if request.user.is_authenticated else (None, None)
    session_key = request.session.session_key
    basket = request.session.get('basket', {})

    # Calculate total and grand total
    total = sum(
        item['quantity'] * item['cake_price']
        for item in basket.values() if 'quantity' in item and 'cake_price' in item
    )
    grand_total = total  # Adjust if necessary for delivery fees or discounts

    context = {
        "basket_items": basket,
        "total": total,
        "grand_total": grand_total,
        "free_delivery_delta": max(0, 50 - total),  # Assuming free delivery above 50 euros
    }
    return render(request, 'basket/basket.html', context)

# View to add a quantity of the specified cake to the shopping basket
def add_to_basket(request, cake_id):
    """ Add a quantity of the specified cake to the shopping basket """

    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse('products'))
    size = None
    if 'cake_size' in request.POST:
        size = request.POST['cake_size']
    basket = request.session.get('basket', {})

    if size:
        if cake_id in basket:
            if 'items_by_size' not in basket[cake_id]:
                basket[cake_id]['items_by_size'] = {}
            if size in basket[cake_id]['items_by_size']:
                basket[cake_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {cake.name} quantity to {basket[cake_id]["items_by_size"][size]}')
            else:
                basket[cake_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {cake.name} to your basket')
        else:
            basket[cake_id] = {'items_by_size': {size: quantity}, 'cake_price': float(cake.price)}
            messages.success(request, f'Added size {size.upper()} {cake.name} to your basket')
    else:
        if cake_id in basket:
            basket[cake_id]['quantity'] += quantity
            messages.success(request, f'Updated {cake.name} quantity to {basket[cake_id]["quantity"]}')
        else:
            basket[cake_id] = {'quantity': quantity, 'cake_price': float(cake.price)}
            messages.success(request, f'Added {cake.name} to your basket')

    # Save the updated basket to the session
    request.session['basket'] = basket
    return redirect(redirect_url)

# View to update the quantity of a specified cake in the basket
def update_basket(request, cake_id):
    """ Update the quantity of the specified cake in the shopping basket """
    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('cake_size', None)
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[cake_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {cake.name} quantity to {basket[cake_id]["items_by_size"][size]}')
        else:
            del basket[cake_id]['items_by_size'][size]
            if not basket[cake_id]['items_by_size']:
                basket.pop(cake_id)
            messages.success(request, f'Removed size {size.upper()} {cake.name} from your basket')
    else:
        if quantity > 0:
            basket[cake_id]['quantity'] = quantity
            messages.success(request, f'Updated {cake.name} quantity to {basket[cake_id]["quantity"]}')
        else:
            basket.pop(cake_id)
            messages.success(request, f'Removed {cake.name} from your basket')

    # Save the updated basket to the session
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

# View to remove a cake from the shopping basket
def remove_from_basket(request, cake_id):
    """ Remove the specified cake from the shopping basket """
    try:
        cake = get_object_or_404(Cake, pk=cake_id)
        size = request.POST.get('cake_size', None)
        basket = request.session.get('basket', {})

        if size:
            del basket[cake_id]['items_by_size'][size]
            if not basket[cake_id]['items_by_size']:
                basket.pop(cake_id)
            messages.success(request, f'Removed size {size.upper()} {cake.name} from your basket')
        else:
            basket.pop(cake_id)
            messages.success(request, f'Removed {cake.name} from your basket')

        # Save the updated basket to the session
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
