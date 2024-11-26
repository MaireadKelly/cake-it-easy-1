from django.shortcuts import render, redirect, get_object_or_404
from home.customer import Customer
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from products.models import Product


def index(request):
    featured_products = Product.objects.all()[
        :3
    ]  # Get the first 3 products, for example
    return render(request, "home/index.html", {"featured_products": featured_products})


# Shop View
@login_required
def shop(request):
    products = Product.objects.all()
    return render(request, "home/products.html", {"products": products})


# View to show Customer profile
@login_required
def customer_profile(request):
    customer, created = Customer.objects.get_or_create(
        user=request.user
    )  # Automatically create if it doesn't exist
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile")
    else:
        form = CustomerForm(instance=customer)

    context = {"form": form, "customer": customer}

    return render(request, "customer_profile.html", context)


@login_required
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.customer  # Assuming user is logged in
            # if the user didn't provide a delivery address, use their primary address
            if not order.delivery_address:
                order.delivery_address = request.user.customer.address
            order.save()
            return redirect("home:product_list")
    else:
        form = OrderForm()
    return render(request, "home/order_form.html", {"form": form})


def our_story(request):
    return render(request, "home/our_story.html")


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/product_detail.html", {"product": product})
