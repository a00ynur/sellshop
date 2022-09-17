from django.shortcuts import render
from django.http import HttpResponse
from basket.forms import ShippingAddressForm, BillingAddressForm
from django.utils.translation import gettext as _
from basket.models import BasketItem, BillingAddress, ShippingAddress, Basket
from datetime import datetime
from product.models import ProductVersion

def wishlist(request):
    if request.user.is_authenticated:
        return render(request, "wishlist.html")
    return render(request, "error-404.html")

    
def cart(request):
    if request.user.is_authenticated:
        return render(request, "cart.html")
    return render(request, "error-404.html")

	
def order(request):
    if request.user.is_authenticated:
        return render(request, "order-complete.html")
    return render(request, "error-404.html")



def checkout(request):
        try:
            cart = BasketItem.objects.filter(
                cart=Basket.objects.get(author=request.user, status=False))
            counter = 0
            for i in range(len(cart)):
                if cart[i].product.quantity > 0:
                    counter += 1
        except:
            counter = 0
        if request.method == "POST":
            form = ShippingAddressForm(request.POST)
            
            shipping = ShippingAddress(
                    user=request.user,
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    address=request.POST.get('address'),
                    city=request.POST.get('city'),
                    zipcode=request.POST.get('zipcode'),
                    country=request.POST.get('country'),
                    phone=request.POST.get('phone'),
                )
            shipping.save()
            basket=Basket.objects.filter(status=False).filter(author=request.user).update(
                    status=True, shipping_address=shipping, ordered_at=datetime.now())
            user_cart = Basket.objects.filter(author=request.user).filter(
                    status=True).filter(shipping_address=shipping).first()
            for i in range(len(BasketItem.objects.filter(basket=user_cart))):
                    

                    quantity = BasketItem.objects.filter(basket=user_cart)[i].productVersion.quantity - BasketItem.objects.filter(basket=user_cart)[i].count
                    ProductVersion.objects.filter(id=BasketItem.objects.filter(
                        basket=user_cart)[i].productVersion.id).update(quantity=quantity)
          
            form = ShippingAddressForm()
        context = {
            'title': 'Checkout Sellshop',
            'shipping': form,
            'cart_products': counter,
        }
        if request.user.is_authenticated:
            return render(request, "checkout.html", context=context)
        return render(request, "error-404.html", context=context)
