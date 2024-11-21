from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Home page route
    path('customer/<int:customer_id>/', views.customer_profile, name='customer_profile'),
    path('order/', views.order_create, name='order_create'),  # Order page
    path('our-story/', views.our_story, name='our_story'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]
