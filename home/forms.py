from django import forms
from .models import Order, Comment, Rating
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'preview_description', 'description', 'price', 'slug', 'category', 'image']

class OrderForm(forms.ModelForm):
    delivery_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))  # Date and time picker
    class Meta:
        model = Order
        fields = ["product", "quantity", "inscription", "delivery_time", "delivery_address"]  # Only order-related fields


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # Only the comment content is needed


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]  # Only the rating field
