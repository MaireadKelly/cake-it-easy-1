# shop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Customer, Comment, Rating
from .forms import OrderForm, CommentForm, RatingForm
from django.contrib.auth.decorators import login_required
from products.models import Product, Cake


def index(request):
    return render(request, "home/index.html")


# View to show Customer profile
@login_required
def customer_profile(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, "home/customer_profile.html", {"customer": customer})

# Shop View
def shop(request):
    products = Product.objects.all()
    return render(request, 'home/shop.html', {'products': products})


# Product detail view
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    ratings = product.ratings.all()

    return render(request, 'home/product_detail.html', {'product': product, 'comments': comments, 'ratings': ratings})


# View to Add New Product
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('home:product_detail.html', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'home/add_product.html', {'form': form})


# View to edit existing product
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home:product_detail.html')
    else:
        form = ProductForm(instance=product)
    return render(request, 'home/edit_product.html', {'form': form})


# View to delete a product
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('shop')
    return render(request, 'home/delete_product.html', {'product': product})


def product_list(request):
    products = Product.objects.all()
    return render(request, "home/product_list.html", {"products": products})


@login_required
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user.customer # Assuming user is logged in
            # if the user didn't provide a delivery address, use their primary address
            if not order.delivery_address:
                order.delivery_address = request.user.customer.address
            order.save()
            return redirect("home:product_list")
    else:
        form = OrderForm()
    return render(request, "home/order_form.html", {"form": form})


# View to handle adding comments
@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.customer = request.user.customer  # Assuming user is logged in
            comment.product = product
            comment.save()
            return redirect("home:product_detail", pk=product.id)

    else:
        form = CommentForm()
    return render(request, "home/add_comment.html", {"form": form, "product": product})


# View to handle adding ratings
@login_required
def add_rating(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.customer = request.user.customer
            rating.product = product
            rating.save()
            return redirect("home:product_detail", pk=product.id)

    else:
        form = RatingForm()
    return render(request, 'home/add_rating.html', {'form': form, 'product': product})


def our_story(request):
    return render(request, 'home/our_story.html')



