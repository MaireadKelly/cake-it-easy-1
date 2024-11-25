from django import forms
from .models import Product, CustomCake, Cake
from home.models import Comment, Rating

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'preview_description', 'description', 'price', 'category', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        
class CustomCakeForm(forms.ModelForm):
    class Meta:
        model = CustomCake
        fields = ['flavor', 'filling', 'inscription', 'price', 'image']
        
class Cake(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['occasion', 'name', 'description', 'price', 'image', 'category']
