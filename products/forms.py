from django import forms
from .models import Product, CustomCake, Cake, CakeSize
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
    sizes = forms.ModelMultipleChoiceField(
        queryset=CakeSize.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = CustomCake
        fields = ['flavor', 'filling', 'inscription', 'sizes', 'price', 'image']

class CakeForm(forms.ModelForm):
    sizes = forms.ModelMultipleChoiceField(
        queryset=CakeSize.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Cake
        fields = ['occasion', 'name', 'description', 'sizes', 'price', 'image', 'category']
