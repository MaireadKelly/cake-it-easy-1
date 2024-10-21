from django.urls import path, include
from . import views
from .views import cake_list, order_create
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),  # Home page route
    path('accounts/', include('allauth.urls')),  # Accounts-related routes
    path('cakes/', cake_list, name='cake_list'),  # Cake listing page with a different URL
    path('order/', order_create, name='order_create'),  # Order page
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
