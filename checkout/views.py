import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Order, OrderLineItem
from .forms import OrderForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Cake
from basket.contexts import basket_contents

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "basket": json.dumps(request.session.get("basket", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be \
            processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    basket = request.session.get("basket", {})
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect("products")

    current_basket = basket_contents(request)
    total = current_basket["grand_total"]
    stripe_total = round(total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            client_secret = request.POST.get("client_secret")
            if not client_secret:
                messages.error(request, "Client secret missing. Please try again.")
                return redirect("checkout")

            pid = client_secret.split("_secret")[0]
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
                    for size, quantity in item_data["items_by_size"].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            cake=cake,
                            quantity=quantity,
                            cake_size=size,
                        )
                        order_line_item.save()

            request.session["basket"] = {}
            messages.success(request, "Order successfully processed!")
            return redirect("order_confirmation", order_number=order.order_number)
        else:
            messages.error(
                request,
                "There was an error with your form. Please double-check your information.",
            )

    else:
        form = OrderForm()

    context = {
        "form": form,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret if intent else "",
    }

    return render(request, "checkout/checkout.html", context)


@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Handle the event
    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        print(f"Payment for {payment_intent['amount']} succeeded.")
    elif event["type"] == "payment_intent.payment_failed":
        payment_intent = event["data"]["object"]
        print(f"Payment for {payment_intent['amount']} failed.")

    return HttpResponse(status=200)


def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    context = {"order": order}
    return render(request, "checkout/order_confirmation.html", context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "basket" in request.session:
        del request.session["basket"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
