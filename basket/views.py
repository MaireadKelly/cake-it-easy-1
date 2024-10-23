from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket, BasketItem
from home.models import Cake

# Create your views here.

def add_to_basket(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    customer = request.user.customer if request.user.is_authenticated else None
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    basket, created = Basket.objects.get_or_create(customer=customer, session_key=session_key)
    item, created = BasketItem.objects.get_or_create(basket=basket, cake=cake)
    if not created:
        item.quantity += 1  # Increase the quantity if the item already exists
    item.save()

    return redirect('view_basket')


def view_basket(request):
    customer = request.user.customer if request.user.is_authenticated else None
    session_key = request.session.session_key
    basket = Basket.objects.filter(customer=customer, session_key=session_key).first()
    
    return render(request, 'basket/view_basket.html', {'basket': basket})


def update_basket(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        item.quantity = new_quantity
        item.save()
    
    return redirect('view_basket')
