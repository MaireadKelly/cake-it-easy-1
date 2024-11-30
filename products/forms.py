from django import forms
from .models import Product, Cake, CustomCake, CakeSize


class CakeForm(forms.ModelForm):
    sizes = forms.ModelMultipleChoiceField(
        queryset=CakeSize.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Cake
        fields = ["name", "description", "sizes", "price", "image", "category", "occasion"]


class CustomCakeForm(forms.ModelForm):
    sizes = forms.ModelMultipleChoiceField(
        queryset=CakeSize.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = CustomCake
        fields = ["flavor", "filling", "sizes", "price", "image", "inscription"]


class CakeSizeForm(forms.ModelForm):
    class Meta:
        model = CakeSize
        fields = ["name", "description", "price"]
