from django import forms
from .models import Order, Comment, Rating
from products.models import Product
from home.customer import Customer
from allauth.account.forms import SignupForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'preview_description', 'description', 'price', 'slug', 'category', 'image']

class OrderForm(forms.ModelForm):
    delivery_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))  # Date and time picker
    class Meta:
        model = Order
        fields = ["product", "quantity", "inscription", "delivery_time", "delivery_address"]  # Only order-related fields
        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'phone_number', 'email']  # Add other fields as needed
        

class CustomSignupForm(SignupForm):
    # Default fields provided by Allauth (username, email, password) are already included
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    address = forms.CharField(max_length=255, required=True, label="Address")
    phone_number = forms.CharField(max_length=20, required=False, label="Phone Number")

    def save(self, request):
        # Save the user using the default Allauth save method
        user = super().save(request)
        
        # Save additional fields to the Customer model
        Customer.objects.create(
            user=user,
            address=self.cleaned_data['address'],
            phone_number=self.cleaned_data['phone_number'],
        )
        
        # Update user's first and last name
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # Only the comment content is needed


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]  # Only the rating field
