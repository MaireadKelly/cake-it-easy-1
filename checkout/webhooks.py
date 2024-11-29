import json
import stripe
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from checkout.models import Order
from profiles.models import UserProfile

@csrf_exempt
def stripe_webhook(request):
    """
    Listen for webhooks from Stripe
    """
    # Set up Stripe API key
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook secret from settings
    webhook_secret = settings.STRIPE_WH_SECRET

    # Get the request payload and headers
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    # Create an empty event
    event = None

    try:
        # Verify the webhook signature to ensure it came from Stripe
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event type
    if event and event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']

        # Retrieve payment intent details
        client_secret = payment_intent['client_secret']
        billing_details = payment_intent['charges']['data'][0]['billing_details']
        shipping_details = payment_intent['shipping']

        # Assuming metadata is used to pass the order number
        order_number = payment_intent['metadata']['order_number']

        # Fetch the order and update status
        order = Order.objects.get(order_number=order_number)
        if order:
            order.stripe_pid = payment_intent.id
            order.original_bag = json.dumps(payment_intent['metadata'])
            order.save()

    elif event and event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        print(f"Payment failed for PaymentIntent {payment_intent.id}")

    # Add more event types here as needed, like 'checkout.session.completed'

    return HttpResponse(status=200)
