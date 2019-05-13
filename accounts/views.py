from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
	return HttpResponse("home")
def signup(request):
	if request.method == 'POST':
		#User is signing up
		#check if passwords match
		if request.POST['password'] == request.POST['password-confirm']:
			try:
				#Check if user exists
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'Username already exists'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
				auth.login(request,user)
				return redirect('producthunt_home')
		else:
			return render(request, 'accounts/signup.html', {'error':'Passwords Must Match'})
	else:
		#User wants to get signup page
		return render(request,'accounts/signup.html')
def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('producthunt_home')
		else:
			return render(request, 'accounts/login.html',{'error':'Username or Password is incorrect.'})
	else:
		return render(request,'accounts/login.html')
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('producthunt_home')