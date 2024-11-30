from django.urls import path
from . import views

urlpatterns = [
    # All products listing page
    path("", views.all_products, name="products"),
    # Product detail page
    path("<int:pk>/", views.product_detail, name="product_detail"),
    # Add, edit, and delete product
    path("add/", views.add_product, name="add_product"),
    path("<int:pk>/edit/", views.edit_product, name="edit_product"),
    path("<int:pk>/delete/", views.delete_product, name="delete_product"),
    # Add comment and rating
    path("<int:product_id>/comment/", views.add_comment, name="add_comment"),
    path("<int:product_id>/rating/", views.add_rating, name="add_rating"),
    # Custom Cake Order
    path("custom-cake-order/", views.custom_cake_order, name="custom_cake_order"),
]
