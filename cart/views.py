from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

#Cart Summary View
def cart_summary(request):
    return render(request, 'cart/summary.html', {

})


#Cart Add View
def cart_add(request):
    #Get the Cart
    cart = Cart(request)
    #Test for Post
    if request.POST.get('action') == 'post':
        #Get Stuff
        product_id = int(request.POST.get('product_id'))

        #Look up Product in the Database
        product = get_object_or_404(Product, id=product_id)

        #Save to Session
        cart.add(product=product)

        #Get Cart Quantity
        cart_quantity = cart.__len__()

        #Return Response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response

#Cart Delete View
def cart_delete(request):
    pass

#Cart Update View
def cart_update(request):
    pass