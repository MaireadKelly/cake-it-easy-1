# forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    delivery_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))  # Date and time picker
    
    class Meta:
        model = Order
        fields = ['cake', 'quantity', 'inscription', 'delivery_time']
