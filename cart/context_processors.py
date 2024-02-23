from .cart import Cart

#Create Context processor so our car can work on all page.
def cart(request):
    return{'cart': Cart(request)}