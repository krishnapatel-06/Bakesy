from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Bakesy/home.html')

def products(request):
    return render(request,'Bakesy/products.html')
def order(request):
    return render(request,'Bakesy/order.html')
def about(request):
    return render(request,'Bakesy/about.html')
def location(request):
    return render(request,'Bakesy/location.html')
def error(request):
    return render(request,'Bakesy/error.html')