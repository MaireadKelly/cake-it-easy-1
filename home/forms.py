
from django import forms

from .models import Order, Comment, Rating



class OrderForm(forms.ModelForm):

    delivery_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))  # Date and time picker

    

    class Meta:

        model = Order

        fields = ['cake', 'quantity', 'inscription', 'delivery_time']  # Only order-related fields



class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ['content']  # Only the comment content is needed



class RatingForm(forms.ModelForm):

    class Meta:

        model = Rating

        fields = ['rating']  # Only the rating field