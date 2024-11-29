from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product  # Update to match your project
from decimal import Decimal

def basket_contents(request):
    """
    Makes the basket contents available globally in templates.
    """
    basket = request.session.get('basket', {})

    basket_items = []
    total = 0
    product_count = 0

    for item_id, item_data in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, int):
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'product': product,
                'quantity': item_data,
                'subtotal': item_data * product.price,
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'product': product,
                    'quantity': quantity,
                    'size': size,
                    'subtotal': quantity * product.price,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_COST
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
