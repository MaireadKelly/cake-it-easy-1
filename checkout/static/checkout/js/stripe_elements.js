/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

document.addEventListener('DOMContentLoaded', function() {
    // Get Stripe public key and client secret from hidden inputs
    var stripePublicKey = document.getElementById("id_stripe_public_key").value;
    var clientSecret = document.getElementById("id_client_secret").value;

    console.log("Stripe Public Key:", stripePublicKey);
    console.log("Client Secret:", clientSecret);

    // Set up Stripe.js and Elements to use in checkout form
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();

    // Custom styling can be passed to the Stripe Elements.
    var style = {
        base: {
            color: "#32325d",
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: "antialiased",
            fontSize: "16px",
            "::placeholder": {
                color: "#aab7c4"
            }
        },
        invalid: {
            color: "#fa755a",
            iconColor: "#fa755a"
        }
    };

    // Create an instance of the card Element.
    var card = elements.create("card", {style: style});
    card.mount("#card-element");

    // Handle real-time validation errors on the card Element
    card.addEventListener('change', function(event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            errorDiv.textContent = event.error.message;
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handle form submission
    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function(ev) {
        ev.preventDefault();

        // Disable form elements and show loading
        card.update({ 'disabled': true });
        document.getElementById('submit-button').disabled = true;
        document.getElementById('loading-overlay').classList.remove('d-none');

        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: document.getElementById('full_name').value,
                    email: document.getElementById('email').value,
                    phone: document.getElementById('phone_number').value,
                    address: {
                        line1: document.getElementById('address').value,
                        city: document.getElementById('city').value,
                    }
                }
            },
            shipping: {
                name: document.getElementById('full_name').value,
                phone: document.getElementById('phone_number').value,
                address: {
                    line1: document.getElementById('address').value,
                    city: document.getElementById('city').value,
                }
            }
        }).then(function(result) {
            if (result.error) {
                // Display error message
                document.getElementById('card-errors').textContent = result.error.message;

                // Re-enable form elements
                card.update({ 'disabled': false });
                document.getElementById('submit-button').disabled = false;
                document.getElementById('loading-overlay').classList.add('d-none');
            } else {
                // Payment successful, submit the form
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    });
});
