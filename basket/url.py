from django.urls import URLPattern
from django.urls import path
from . import views
from basket.views import wishlist, order, checkout, cart

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('checkout/', checkout, name='checkout'),
    path('order/', order, name='order'),

]

