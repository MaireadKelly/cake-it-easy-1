# shop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cake, Order, Customer, Comment, Rating
from .forms import OrderForm, CakeForm, CommentForm, RatingForm


def index(request):
    return render(request, "home/index.html")


# View to show Customer profile
def customer_profile(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, "home/customer_profile.html", {"customer": customer})


def shop(request):
    cakes = Cake.objects.all()
    return render(request, 'home/shop.html', {'cakes: cakes'})


# View to Add New Cake
def add_cake(request):
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = CakeForm()
    return render(request, 'home/add_cake.html', {'form': form})


# View to edit existing cake
def edit_cake(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES, instance=cake)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = CakeForm(instance=cake)
    return render(request, 'home/edit_cake.html', {'form': form})


# View to delete a cake
def delete_cake(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    if request.method == 'POST':
        cake.delete()
        return redirect('shop')
    return render(request, 'home/delete_cake.html', {'cake': cake})


def cake_list(request):
    cakes = Cake.objects.all()
    return render(request, "home/cake_list.html", {"cakes": cakes})


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
            return redirect("cake_list")
    else:
        form = OrderForm()
    return render(request, "home/order_form.html", {"form": form})


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
    return render(request, "home/add_comment.html", {"form": form, "cake": cake})


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
    return render(request, 'home/add_rating.html', {'form': form, 'cake': cake})


def shop(request):
    cakes = Cake.objects.all() # Retrieve All cakes
    return render(request, 'home/shop.html', {'cakes': cakes})


def our_story(request):
    return render(request, 'home/our_story.html')



