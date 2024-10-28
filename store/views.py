from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserFrom, UpdatePasswordForm

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


#Category View
def category(request, foo):
    #replace Hyphens with Space
    foo = foo.replace('-', ' ')
    #Grab the Category fronm the URL
    try:
        #Look Up The Category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'store/category.html', {
            'products':products, 'category':category
        })
    except:
        messages.success(request, ('That Category doesnt exist'))
        return redirect('home')


#Admin Dashbord View
def admin_dashboard(request):
    return render(request, 'store/admin_dashboard.html' , {
            
    })


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'store/category_summary.html',{
        'categories':categories
    })


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserFrom(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "Profile Updated Successfully!!")
            return redirect('home')
        return render(request, 'store/update_user.html',  {'user_form': user_form})
    else:
        messages.success(request, "You need to login to see this page")
        return redirect('home')
   
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
         # Did they fill out the form
        if request.method == "POST":
            form = UpdatePasswordForm(current_user, request.POST)
            #Is the form valid 
            if form.is_valid():
             form.save()
             messages.success(request, "Your Password has changed Successfully")
             #login(request, current_user)
             return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'store/update_password.html', {'form':form})
    else:
        messages.success(request, "You Need to Login to see his page")
        return redirect('home')
   