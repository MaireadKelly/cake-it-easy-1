from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),  # All products listing page
    path('products/', views.all_products, name='product_list'),  # All products listing page
    path('add/', views.add_product, name='add_product'),  # Add new product
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),  # Edit product
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),  # Delete product
    path('<int:pk>/', views.product_detail, name='product_detail'),  # Product detail page
    path('<int:product_id>/comment/', views.add_comment, name='add_comment'),  # Add comment
    path('<int:product_id>/rating/', views.add_rating, name='add_rating'),  # Add rating
]
