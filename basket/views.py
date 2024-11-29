from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Cake

# View that renders the basket contents page
def view_basket(request):
    context = {
        'body-class': 'basket/basket.html'
    }
    """ A view that renders the basket contents page """
    return render(request, 'basket/basket.html', context)

# View to add a quantity of the specified cake to the shopping basket
def add_to_basket(request, cake_id):
    """ Add a quantity of the specified cake to the shopping basket """

    # Get the cake instance
    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url', reverse('view_basket'))  # Default redirect URL
    size = None
    if 'cake_size' in request.POST:
        size = request.POST['cake_size']
    
    # Get the basket session or create a new one if not exist
    basket = request.session.get('basket', {})

    # Handle the case where quantity is missing
    if not quantity:
        messages.error(request, "Quantity not specified. Please try again.")
        return redirect(redirect_url)
    
    # Convert quantity to an integer and validate it
    try:
        quantity = int(quantity)
        if quantity <= 0:
            messages.error(request, "Please enter a valid quantity.")
            return redirect(redirect_url)
    except ValueError:
        messages.error(request, "Invalid quantity. Please enter a valid number.")
        return redirect(redirect_url)

    # Adding items to basket with or without a specific size
    if size:
        if str(cake_id) in basket:
            if size in  basket[str(cake_id)]['items_by_size']:
                basket[str(cake_id)]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {cake.name} quantity to {basket[str(cake_id)]["items_by_size"][size]}')
            else:
                basket[str(cake_id)]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {cake.name} to your basket')
        else:
            basket[str(cake_id)] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {cake.name} to your basket')
    else:
        if str(cake_id) in basket:
            basket[str(cake_id)] += quantity
            messages.success(request, f'Updated {cake.name} quantity to {basket[str(cake_id)]}')
        else:
            basket[str(cake_id)] = quantity
            messages.success(request, f'Added {cake.name} to your basket')

    # Save the updated basket to the session
    request.session['basket'] = basket
    return redirect(redirect_url)

# View to update the quantity of a specified cake in the basket
def update_basket(request, cake_id):
    """ Adjust the quantity of the specified cake in the shopping basket """

    cake = get_object_or_404(Cake, pk=cake_id)
    quantity = request.POST.get('quantity')
    size = None
    if 'cake_size' in request.POST:
        size = request.POST['cake_size']
    
    # Get the basket session or create a new one if not exist
    basket = request.session.get('basket', {})

    # Handle the case where quantity is missing
    if not quantity:
        messages.error(request, "Quantity not specified. Please try again.")
        return redirect('view_basket')

    # Convert quantity to an integer and validate it
    try:
        quantity = int(quantity)
        if quantity < 0:
            messages.error(request, "Please enter a valid quantity.")
            return redirect('view_basket')
    except ValueError:
        messages.error(request, "Invalid quantity. Please enter a valid number.")
        return redirect('view_basket')

    # Update items in the basket with or without a specific size
    if size:
        if quantity > 0:
            basket[str(cake_id)]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {cake.name} quantity to {basket[str(cake_id)]["items_by_size"][size]}')
        else:
            del basket[str(cake_id)]['items_by_size'][size]
            if not basket[str(cake_id)]['items_by_size']:
                basket.pop(str(cake_id))
            messages.success(request, f'Removed size {size.upper()} {cake.name} from your basket')
    else:
        if quantity > 0:
            basket[str(cake_id)] = quantity
            messages.success(request, f'Updated {cake.name} quantity to {basket[str(cake_id)]}')
        else:
            basket.pop(str(cake_id))
            messages.success(request, f'Removed {cake.name} from your basket')

    # Save the updated basket to the session
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

# View to remove a cake from the shopping basket
def remove_from_basket(request, cake_id):
    """ Remove the specified cake from the shopping basket """

    try:
        cake = get_object_or_404(Cake, pk=cake_id)
        size = None
        if 'cake_size' in request.POST:
            size = request.POST['cake_size']
        
        # Get the basket session or create a new one if not exist
        basket = request.session.get('basket', {})

        # Remove items from the basket with or without a specific size
        if size:
            del basket[str(cake_id)]['items_by_size'][size]
            if not basket[str(cake_id)]['items_by_size']:
                basket.pop(str(cake_id))
            messages.success(request, f'Removed size {size.upper()} {cake.name} from your basket')
        else:
            basket.pop(str(cake_id))
            messages.success(request, f'Removed {cake.name} from your basket')

        # Save the updated basket to the session
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
