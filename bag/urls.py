from django.urls import path
from . import views

urlpatterns = [
    path("add-to-bag/<int:cake_id>/", views.add_to_bag, name="add_to_bag"),
    path("view-bag/", views.view_bag, name="view_bag"),
    path("update-bag/<int:cake_id>/", views.update_bag, name="update_bag"),
    path(
        "remove-from-bag/<int:cake_id>/",
        views.remove_from_bag,
        name="remove_from_bag",
    ),
]
