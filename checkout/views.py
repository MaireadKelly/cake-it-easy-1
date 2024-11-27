import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderLineItem
from basket.contexts import bag_contents
from .forms import OrderForm

# Create your views here.

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect('products')

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = basket
            order.save()

            for item_id, item_data in basket.items():
                cake = get_object_or_404(Cake, pk=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        cake=cake,
                        quantity=item_data,
                    )
                    order_line_item.save()
                else:
                    for size, quantity in item_data['items_by_size'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            cake=cake,
                            quantity=quantity,
                            cake_size=size,
                        )
                        order_line_item.save()

            request.session['basket'] = {}
            messages.success(request, 'Order successfully processed!')
            return redirect('order_confirmation', order_number=order.order_number)
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')

    else:
        form = OrderForm()

    context = {
        'form': form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def order_confirmation(request, order_number):
    """ A view to handle successful order confirmations """
    order = get_object_or_404(Order, order_number=order_number)
    
    context = {
        'order': order,
    }
    
    return render(request, 'checkout/order_confirmation.html', context)
