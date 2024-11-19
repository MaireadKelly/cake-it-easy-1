from django.shortcuts import render
from .forms import ProductForm

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', {'products': products}, context)
"""A view to show all products, including sorting and search queries """