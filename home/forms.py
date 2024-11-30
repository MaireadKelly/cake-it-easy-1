from django import forms
from .models import Order, Comment, Rating
from products.models import Product
from home.customer import Customer
from allauth.account.forms import SignupForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'slug', 'category', 'image']

class OrderForm(forms.ModelForm):
    delivery_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))  # Date and time picker
    class Meta:
        model = Order
        fields = ["product", "quantity", "inscription", "delivery_time", "delivery_address"]  # Only order-related fields
        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone_number', 'street_address1', 'street_address2', 'town_or_city', 'postcode', 'county']
        

class CustomSignupForm(SignupForm):
    address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=20, required=False)

    def save(self, request):
        # Save the User object using Allauth's save method
        user = super().save(request)

        # Check if a Customer profile already exists before creating one
        customer, created = Customer.objects.get_or_create(
            user=user,
            defaults={
                'address': self.cleaned_data.get('address', ''),
                'phone_number': self.cleaned_data.get('phone_number', ''),
            }
        )

        # If a profile already exists, update its fields
        if not created:
            customer.address = self.cleaned_data.get('address', '')
            customer.phone_number = self.cleaned_data.get('phone_number', '')
            customer.save()

        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # Only the comment content is needed


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]  # Only the rating field
