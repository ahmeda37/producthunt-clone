from django.shortcuts import render

def home(request):
	return render(request,'producthunt/home.html')