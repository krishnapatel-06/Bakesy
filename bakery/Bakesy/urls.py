from django.urls import path
from Bakesy import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('products/',views.products,name='products'),
    path('order/',views.order,name = 'order'),
    path('about/',views.about,name='about'),
    path('location/',views.location,name = 'location'),
    path('error/',views.error,name = 'error')
]