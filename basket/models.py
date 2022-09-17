from distutils.command.upload import upload 
from django.db import models
from django.contrib.auth import get_user_model
from product.models import ProductVersion

USER = get_user_model()
# Create your models here.

class Basket(models.Model):
    author = models.ForeignKey(USER, default='', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.status)


class ShippingAddress(models.Model):
    user        = models.ForeignKey(USER, on_delete=models.CASCADE,related_name="shipping_address")

    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    address   =   models.CharField(max_length=100)
    city        = models.CharField(max_length=50)
    zipcode     = models.CharField(max_length=50)
    country     = models.CharField(max_length=50)
    phone       = models.CharField(max_length=50)

    def __str__(self):
        return str(self.address)

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"

class BillingAddress(models.Model):
    user        = models.ForeignKey(USER, on_delete=models.CASCADE, default='',related_name="billing_address")

    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    address     = models.CharField(max_length=255)
    city        = models.CharField(max_length=255)
    zipcode     = models.CharField(max_length=255)
    country     = models.CharField(max_length=255)
    phone       = models.CharField(max_length=255)

    def __str__(self):
        return self.address


    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    productVersion = models.ForeignKey(ProductVersion, on_delete=models.CASCADE)
    price = models.ImageField(null=True, blank=True)
    count = models.IntegerField(default=True, null=True, blank=True)

    class Meta:
        verbose_name = "BasketItem"
        verbose_name_plural = "BasketItems"


class Order(models.Model):
    total_price = models.IntegerField(null=True, blank=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)