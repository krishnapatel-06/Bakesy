from django.urls import path
from Bakesy import views


urlpatterns = [
    path('',views.home,name = 'home')
]