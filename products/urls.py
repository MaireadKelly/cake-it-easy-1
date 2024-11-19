from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('products/', views.product_list, name='product_list'),  # Cake listing page
    path('customer/<int:customer_id>/', views.customer_profile, name='customer_profile'),
    path('order/', views.order_create, name='order_create'),  # Order page
    path('our-story/', views.our_story, name='our_story'),
    path('shop/', views.shop, name='shop'),
    path('shop/add/', views.add_product, name='add_product'),
    path('shop/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('shop/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/comment/', views.add_comment, name='add_comment'),
    path('product/<int:product_id>/rating/', views.add_rating, name='add_rating'),
]