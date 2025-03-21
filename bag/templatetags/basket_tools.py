from django import template
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product  # Update to match your project
from decimal import Decimal

register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    """
    Template filter to calculate the subtotal of a product
    """
    return price * quantity


@register.inclusion_tag("bag/bag_summary.html", takes_context=True)
def bag_summary(context):
    """
    Custom inclusion tag to provide bag summary details in templates.
    """
    request = context["request"]
    bag = request.session.get("bag", {})

    bag_items = []
    total = 0
    product_count = 0

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, int):
            total += item_data * product.price
            product_count += item_data
            bag_items.append(
                {
                    "product": product,
                    "quantity": item_data,
                    "subtotal": item_data * product.price,
                }
            )
        else:
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append(
                    {
                        "product": product,
                        "quantity": quantity,
                        "size": size,
                        "subtotal": quantity * product.price,
                    }
                )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_COST
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
