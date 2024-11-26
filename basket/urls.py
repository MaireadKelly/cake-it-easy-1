from django.urls import path
from . import views

urlpatterns = [
    path('add-to-basket/<int:cake_id>/', views.add_to_basket, name='add_to_basket'),
    path('view-basket/', views.view_basket, name='view_basket'),
    path('update-basket/<int:item_id>/', views.update_basket, name='update_basket'),
    path('remove-from-basket/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),  # Added this line
]
