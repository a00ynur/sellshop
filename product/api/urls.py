
from django.urls import path
from product.api.views import ProductAPI


urlpatterns  = [
    path('product/', ProductAPI.as_view(), name="api_product"),
    path('product/<int:pk>/', ProductAPI.as_view (), name="api_product"), 

]