from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Cake


def basket_contents(request):
    basket_items = []
    total = 0
    cake_count = 0
    basket = request.session.get("basket", {})

    for cake_id, item_data in basket.items():
        cake = get_object_or_404(Cake, pk=cake_id)  # Make sure `cake` is defined here for both branches
        if isinstance(item_data, int):

            # Handle non-sized items
            total += item_data * cake.price
            cake_count += item_data
            basket_items.append({"cake_id": cake_id, "quantity": item_data, "cake": cake,})

        else:
            # Handle items with sizes
            items_by_size = item_data.get("items_by_size", {})
            for size, quantity in items_by_size.items():
                total += quantity * cake.price
                cake_count += quantity
                basket_items.append({"cake_id": cake_id, "quantity": quantity, "cake": cake, "size": size,})

    # Use fixed delivery charge from settings
    delivery = Decimal(getattr(settings, 'STANDARD_DELIVERY_CHARGE', 15.00))
    grand_total = total + delivery

    context = {
        "basket_items": basket_items,
        "total": total,
        "cake_count": cake_count,
        "delivery": delivery,
        "grand_total": grand_total,
    }

    return context
