from django.urls import path, include
from . import views
from .views import cake_list, order_create
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('customer/<int:customer_id>/', views.customer_profile, name='customer_profile'),
    path('cake/<int:cake_id>/comment/', views.add_comment, name='add_comment'),
    path('cake/<int:cake_id>/rating/', views.add_rating, name='add_rating'),
    path('', views.index, name='home'),  # Home page route
    path('accounts/', include('allauth.urls')),  # Accounts-related routes
    path('cakes/', views.cake_list, name='cake_list'),  # Cake listing page
    path('order/', views.order_create, name='order_create'),  # Order page
    path('shop/', views.shop, name='shop'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
