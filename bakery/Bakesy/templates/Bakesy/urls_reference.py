# bakesy/urls.py
# ---------------------------------------------------------------------------
# Add these URL patterns to your project's urls.py (or an app-level urls.py).
# The url names must match the {% url '...' %} tags used in the templates.
# ---------------------------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('',          views.home,     name='home'),
    path('about/',    views.about,    name='about'),
    path('products/', views.products, name='products'),
    path('location/', views.location, name='location'),
    path('order/',    views.order,    name='order'),
]

# ---------------------------------------------------------------------------
# Register the custom 404 handler in your ROOT urls.py (not an app urls.py):
# ---------------------------------------------------------------------------
# handler404 = 'bakesy.views.custom_404'


# ---------------------------------------------------------------------------
# Minimal views.py (same app folder) — replace with your own logic as needed
# ---------------------------------------------------------------------------
# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
#
# def home(request):     return render(request, 'home.html')
# def about(request):    return render(request, 'about.html')
# def products(request): return render(request, 'products.html')
# def location(request): return render(request, 'location.html')
# def order(request):    return render(request, 'order.html')
#
# def custom_404(request, exception):
#     return render(request, 'error.html', status=404)
