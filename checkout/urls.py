from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),  # Checkout view
    path('order-confirmation/<str:order_number>/', views.order_confirmation, name='order_confirmation'),  # Order confirmation view
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
]
