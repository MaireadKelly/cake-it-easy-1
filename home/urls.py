from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Home page route
    path('cake/<int:cake_id>/comment/', views.add_comment, name='add_comment'),
    path('cake/<int:cake_id>/rating/', views.add_rating, name='add_rating'),
    path('cakes/', views.cake_list, name='cake_list'),  # Cake listing page
    path('customer/<int:customer_id>/', views.customer_profile, name='customer_profile'),
    path('order/', views.order_create, name='order_create'),  # Order page
    path('our-story/', views.our_story, name='our_story'),
    path('shop/', views.shop, name='shop'),
    path('shop/add/', views.add_cake, name='add_cake'),
    path('shop/<int:pk>/edit/', views.edit_cake, name='edit_cake'),
    path('shop/<int:pk>/delete/', views.delete_cake, name='delete_cake'),
    path('cakes/<int:pk>/', views.cake_detail, name='cake_detail'),
]
