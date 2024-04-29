from .cart import Cart

# This helps the cart to work on all pages


def cart(request):
    return {'cart': Cart(request)}
