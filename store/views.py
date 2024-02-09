from django.shortcuts import render

# Create your views here.

#Home View

def home(request):
    context = "Welcome to my store"
    return render(request, 'store/index.html', {
        "context":context
    })