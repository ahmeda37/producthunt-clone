from django.shortcuts import render
from products.models import Product

def home(request):
	products = Product.objects
	return render(request,'producthunt/home.html',{'products':products})