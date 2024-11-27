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
        if isinstance(item_data, int):
            cake = get_object_or_404(Cake, pk=cake_id)
            total += item_data * cake.price
            cake_count += item_data
            basket_items.append(
                {
                    "cake_id": cake_id,
                    "quantity": item_data,
                    "cake": cake,
                }
            )
        else:
            for size, quantity in item_data["items_by_size"].items():
                cake = get_object_or_404(Cake, pk=cake_id)
                total += quantity * cake.price
                cake_count += quantity
                basket_items.append(
                    {
                        "cake_id": cake_id,
                        "quantity": quantity,
                        "cake": cake,
                        "size": size,
                    }
                )

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = total + delivery

    context = {
        "basket_items": basket_items,
        "total": total,
        "cake_count": cake_count,
        "delivery": delivery,
        "grand_total": grand_total,
    }

    return context
