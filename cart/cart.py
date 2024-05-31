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

    def add(self, product, quanity):
        product_id = str(product.id)
        product_qty = str(quanity)

        #Logic

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        
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
    
    #setting Quantities for each products
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #get our cart
        ourcart = self.cart
        #Update Dictionary Cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        # delete from dictionary/cart

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True