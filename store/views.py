from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

# Create your views here.

#Home View
def home(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {
        "products":products
    })

#About View
def about(request):
    context = 'about us'
    return render(request,'store/about.html', {
        "context":context
    })

#All Product View
def all_product(request):
    products = Product.objects.all()
    return render(request, 'store/all_products.html', {
        "products":products
    })

#Product Detail View
def product_details(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product_details.html', {
        "product":product
    })

#Login View
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You Have been Logged in...")
            return redirect('home')
        else:
            messages.success(request, "There was an error please try again")

    else:
        return render(request, 'store/login.html', {  

    })

#Logout View
def logout_user(request):
    logout(request)
    messages.success(request, ("You have Successfully Logged Out...."))
    return redirect('home')


#Register View
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Your Registration is Successful"))
            return redirect('login')
        else:
            messages.success(request, ("Oops there an error in your registration"))
            return redirect('register')
        
    else:
        return render(request, 'store/register.html', {
            "form":form
    
    })
