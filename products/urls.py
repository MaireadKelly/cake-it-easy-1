from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("cakes/<slug:slug>/", views.cake_detail, name="cake_detail"),
    path("custom-cake-order/", views.custom_cake_order, name="custom_cake_order"),
    path("sizes/", views.cake_size_list, name="cake_size_list"),
    path("add/", views.add_product, name="add_product"),
    path("<int:pk>/edit/", views.edit_product, name="edit_product"),
    path("<int:pk>/delete/", views.delete_product, name="delete_product"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
]
