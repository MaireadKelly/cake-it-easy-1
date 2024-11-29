/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Retrieve public key and client secret from the hidden inputs in the checkout template
// Simplify to avoid unnecessary slicing and ensure correct format
var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.trim();
console.log("Stripe Public Key Retrieved:", stripePublicKey);

// Initialize Stripe only if the key is valid
if (stripePublicKey) {
    var stripe = Stripe(stripePublicKey);
} else {
    console.error("Stripe public key not found or invalid.");
}


var clientSecret = document.getElementById('id_client_secret')

var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Styling options for Stripe Elements
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create an instance of the card element
var card = elements.create('card', {
    style: style
});
// Mount the card element to the div with id="card-element"
card.mount('#card-element');

// Handle real-time validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    document.getElementById('submit-button').setAttribute('disabled', true);
    document.getElementById('loading-overlay').classList.remove('d-none');

    var saveInfo = Boolean(document.getElementById('id-save-info').checked);
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams(postData)
        })
        .then(function (response) {
            return response.json();
        })
        .then(function () {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: form.full_name.value.trim(),
                        phone: form.phone_number.value.trim(),
                        email: form.email.value.trim(),
                        address: {
                            line1: form.street_address1.value.trim(),
                            line2: form.street_address2.value.trim(),
                            city: form.town_or_city.value.trim(),
                            country: form.country.value.trim(),
                            state: form.county.value.trim(),
                        }
                    }
                },
                shipping: {
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    address: {
                        line1: form.street_address1.value.trim(),
                        line2: form.street_address2.value.trim(),
                        city: form.town_or_city.value.trim(),
                        country: form.country.value.trim(),
                        postal_code: form.postcode.value.trim(),
                        state: form.county.value.trim(),
                    }
                },
            }).then(function (result) {
                if (result.error) {
                    var errorDiv = document.getElementById('card-errors');
                    var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                    errorDiv.innerHTML = html;
                    card.update({
                        'disabled': false
                    });
                    document.getElementById('submit-button').removeAttribute('disabled');
                    document.getElementById('loading-overlay').classList.add('d-none');
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        })
        .catch(function () {
            // Reload the page if there is an error
            location.reload();
        });
});