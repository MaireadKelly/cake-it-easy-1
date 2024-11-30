from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings

from home.customer import Customer  # For Customer model
from home.models import Order  # Import Order model from home app
from home.forms import OrderForm, CustomerForm  # Import OrderForm and CustomerForm from home app

from .models import Cake, CustomCake, CakeSize, Product  # Import models from products app
from .forms import CakeForm, CustomCakeForm  # Import Cake and CustomCake forms


# Homepage view
def index(request):
    delivery_charge = getattr(settings, "STANDARD_DELIVERY_CHARGE", 0)
    featured_products = Product.objects.all()[:3]
    return render(
        request,
        "home/index.html",
        {
            "featured_products": featured_products,
            "delivery_charge": delivery_charge,
        },
    )


# Shop view for listing all products
@login_required
def shop(request):
    products = Product.objects.all()
    return render(request, "products/shop.html", {"products": products})


# Cake detail view
def cake_detail(request, slug):
    cake = get_object_or_404(Cake, slug=slug)
    return render(request, "products/cake_detail.html", {"cake": cake})


# Custom cake order view
@login_required
def custom_cake_order(request):
    if request.method == "POST":
        form = CustomCakeForm(request.POST, request.FILES)
        if form.is_valid():
            custom_cake = form.save(commit=False)
            custom_cake.save()
            form.save_m2m()  # Save many-to-many fields
            return redirect("shop")
    else:
        form = CustomCakeForm()
    return render(request, "products/custom_cake_form.html", {"form": form})


# Cake size list view
def cake_size_list(request):
    sizes = CakeSize.objects.all()
    return render(request, "products/cake_size_list.html", {"sizes": sizes})


# Product detail view
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})


# Add a product
@login_required
def add_product(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shop")
    else:
        form = CakeForm()
    return render(request, "products/add_product.html", {"form": form})


# Edit a product
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = CakeForm(instance=product)
    return render(request, "products/edit_product.html", {"form": form})


# Delete a product
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("shop")
    return render(request, "products/delete_product.html", {"product": product})
