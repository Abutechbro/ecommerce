from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if it exits
        cart = self.session.get('session_key')

        #If the user is new, no session key! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        
        #Make sure cart is available on the page of site
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        #Logic

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        self.session.modified = True


    def __len__(self):
        return len(self.cart)
    
    #See What is in the Cart
    def get_prods(self):
        #Get Ids from Cart
        product_ids = self.cart.keys()
        #Use IDS to lookup products in Database model
        product = Product.objects.filter(id__in=product_ids)
        #Return Looked up Products
        return product

