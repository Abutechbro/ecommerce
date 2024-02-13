from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

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

def logout_user(request):
    logout(request)
    messages.success(request, ("You have Successfully Logged Out...."))
    return redirect('home')