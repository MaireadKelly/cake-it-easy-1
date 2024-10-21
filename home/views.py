# shop/views.py

from django.shortcuts import render, redirect
from .models import Cake, Order
from .forms import OrderForm

def index(request):
    return render(request, 'home/index.html')

def cake_list(request):
    cakes = Cake.objects.all()
    return render(request, 'shop/cake_list.html', {'cakes': cakes})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cake_list')
    else:
        form = OrderForm()
    return render(request, 'shop/order_form.html', {'form': form})
