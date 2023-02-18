from django.shortcuts import redirect, render
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import authenticate,login,logout

def register(request):
	form=CustomUserForm()
	if request.method=='POST':
		form=CustomUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Registration Successs You Can Login Now..!")
			return redirect('/login')
	return render(request,"shop/register.html",{"form":form})
def index(request):
	products=Product.objects.filter(trending=1)
	return render(request,"shop/index.html",{"products":products})

def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")

def login_page(request):
	if request.user.is_authenticated:
		return redirect("/")
	else:
		if request.method=='POST':
			name=request.POST.get('username')
			pwd=request.POST.get('password')
			user=authenticate(request,username=name,password=pwd)
			if user is not None:
				login(request,user)
				messages.error(request,"Logged in Successfully")
				return redirect("/")
			else:
				messages.error(request,"Invalid User Name or Password")
				return redirect("/login")
		return render(request,"shop/login.html")

def collections(request):
	catagory=Catagory.objects.filter(status=0)
	return render(request,"shop/collections.html",{"catagory":catagory})
def collectionsview(request,name):
	if(Catagory.objects.filter(name=name,status=0)):
		products=Product.objects.filter(catagory__name=name)
		return render(request,"shop/products/index.html",{"products":products,"category_name":name})
	else:
		messages.warning(request,"No Such Catagory Found")
		return redirect('collections')

def product_details(request):
	return render(request,"shop/product_details.html")