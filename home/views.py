# shop/views.py

from django.shortcuts import render, redirect
from .models import Cake, Order, Customer, Comment, Rating
from .forms import OrderForm, CommentForm, RatingForm


def index(request):
    return render(request, "home/index.html")


# View to show Customer profile
def customer_profile(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, "shop/customer_profile.html", {"customer": customer})


def cake_list(request):
    cakes = Cake.objects.all()
    return render(request, "shop/cake_list.html", {"cakes": cakes})


def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cake_list")
    else:
        form = OrderForm()
    return render(request, "shop/order_form.html", {"form": form})


# View to handle adding comments
def add_comment(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.customer = request.user.customer  # Assuming user is logged in
            comment.cake = cake
            comment.save()
            return redirect("cake_detail", cake_id=cake.id)
    else:
        form = CommentForm()
    return render(request, "shop/add_comment.html", {"form": form, "cake": cake})


# View to handle adding ratings
def add_rating(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.customer = request.user.customer
            rating.cake = cake
            rating.save()
            return redirect('cake_detail', cake_id=cake.id)
    else:
        form = RatingForm()
    return render(request, 'shop/add_rating.html', {'form': form, 'cake': cake})
