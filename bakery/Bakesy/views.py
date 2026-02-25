from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Bakesy/home.html')

def products(request):
    return render(request,'Bakesy/products.html')