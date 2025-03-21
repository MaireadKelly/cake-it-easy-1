from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Cake


def bag_contents(request):
    """
    Context processor to make bag contents available across all templates.
    """
    bag_items = []
    total = 0
    cake_count = 0
    bag = request.session.get("bag", {})

    for cake_id, item_data in bag.items():
        cake = get_object_or_404(Cake, pk=cake_id)

        # If item_data is an integer, it means it's a simple quantity
        if isinstance(item_data, int):
            total += item_data * cake.price
            cake_count += item_data
            bag_items.append(
                {
                    "cake_id": cake_id,
                    "quantity": item_data,
                    "cake": cake,
                }
            )

        # If item_data is a dictionary, it indicates that items have specific sizes
        elif isinstance(item_data, dict) and "items_by_size" in item_data:
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * cake.price
                cake_count += quantity
                bag_items.append(
                    {
                        "cake_id": cake_id,
                        "quantity": quantity,
                        "cake": cake,
                        "size": size,
                    }
                )
        else:
            # Handle unexpected format for item_data gracefully
            continue

    # Set a standard delivery charge (not based on a percentage)
    delivery = Decimal(settings.STANDARD_DELIVERY_CHARGE)

    grand_total = total + delivery

    context = {
        "bag_items": bag_items,
        "total": total,
        "cake_count": cake_count,
        "delivery": delivery,
        "grand_total": grand_total,
    }

    return context
