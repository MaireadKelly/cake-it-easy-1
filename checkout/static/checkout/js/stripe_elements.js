/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", function () {
            // Retrieve public key and client secret from the hidden inputs in the checkout template
            // Retrieve public key and client secret from the hidden inputs in the checkout template
            var stripePublicKeyElement = document.getElementById('id_stripe_public_key');
            if (stripePublicKeyElement) {
                var stripePublicKey = stripePublicKeyElement.value.trim();
                console.log("Stripe Public Key Retrieved:", stripePublicKey); // Log public key to confirm retrieval
            } else {
                console.error("Stripe Public Key element not found in DOM");
                return;
            }

            var clientSecretElement = document.getElementById('id_client_secret');
            if (clientSecretElement) {
                var clientSecret = clientSecretElement.value.trim();
                console.log("Client Secret Retrieved:", clientSecret); // Log client secret to confirm retrieval
            } else {
                console.error("Client Secret element not found in DOM");
                return;
            }


            // Initialize Stripe
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
            var stripe = Stripe(stripePublicKey);
            var elements = stripe.elements();
            console.log("Stripe initialized:", stripe); // Log to verify Stripe is initialized
            console.log("Elements instance created:", elements); // Log to verify elements instance


            // Handle real-time validation errors on the card element
            card.addEventListener('change', function (event) {
                console.log("Card element changed:", event); // Log changes to the card element
                var errorDiv = document.getElementById('card-errors');
                if (event.error) {
                    var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
                    errorDiv.innerHTML = html;
                    console.error("Validation Error:", event.error.message); // Log validation errors
                } else {
                    errorDiv.textContent = '';
                    console.log("Card input is valid"); // Log if input is valid
                }
            });


            // Handle form submission
            var form = document.getElementById('payment-form');

            form.addEventListener('submit', function (ev) {
                ev.preventDefault();
                console.log("Form submitted, starting payment process"); // Log when form submission is initiated

                card.update({
                    'disabled': true
                });
                document.getElementById('submit-button').setAttribute('disabled', true);
                document.getElementById('loading-overlay').classList.remove('d-none');

                var saveInfo = Boolean(document.getElementById('id-save-info').checked);
                console.log("Save info status:", saveInfo); // Log save info checkbox status

                var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
                console.log("CSRF Token:", csrfToken); // Log CSRF Token to ensure it is present

                var postData = {
                    'csrfmiddlewaretoken': csrfToken,
                    'client_secret': clientSecret,
                    'save_info': saveInfo,
                };
                console.log("Post Data:", postData); // Log post data before sending

                var url = '/checkout/cache_checkout_data/';
                fetch(url, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        },
                        body: new URLSearchParams(postData)
                    })
                    .then(function (response) {
                        console.log("Cache checkout data response:", response); // Log response from cache endpoint
                        return response.json();
                    })
                    .then(function () {
                        console.log("Payment confirmed, starting Stripe confirmation"); // Log before confirming payment
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
                                console.error("Payment Error:", result.error.message); // Log error if payment fails
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
                                    console.log("Payment Succeeded!"); // Log when payment is successful
                                    form.submit();
                                }
                            }
                        });
                    })
                    .catch(function (error) {
                        console.error("Error during fetch or Stripe confirmation:", error); // Log fetch errors
                        // Reload the page if there is an error
                        location.reload();
                    });
            });