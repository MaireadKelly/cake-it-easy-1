from django import forms
from .models import Order, Comment, Rating, Cake


class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['name', 'description', 'price', 'slug', 'category', 'image']

class OrderForm(forms.ModelForm):
    delivery_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))  # Date and time picker
    class Meta:
        model = Order
        fields = ["cake", "quantity", "inscription", "delivery_time", "delivery_address"]  # Only order-related fields


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # Only the comment content is needed


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]  # Only the rating field
