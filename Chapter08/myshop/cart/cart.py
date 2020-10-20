from decimal import Decimal
from django.conf import settings

from shop.models import Product


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, overrider_quantity=False):
        """
        Add a product to the cart or update its quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0, 'price': str(product.price)}
        if overrider_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session modified to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum([Decimal(item['price']) * Decimal(item['quantity'])
                    for item in self.cart.values()])

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.cart = {}
        self.save()

    def __iter__(self):
        """
        Iterate over cart items and get them from database
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['quantity'] * item['price']
            yield item

    def __len__(self):
        """
        Count all items
        """
        return sum([item['quantity'] for item in self.cart.values()])
