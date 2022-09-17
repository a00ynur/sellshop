from django import forms 
from basket.models import BillingAddress, ShippingAddress


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = [
            'user',
            'first_name',
            'last_name',
            'address',
            'city',
            'zipcode',
            'country',
            'phone',]

        widgets = {
            'user' : forms.Select(attrs={
                'class' : 'form-control'
            }), 
            'first-name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'address' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'city' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'zipcode' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'country' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'phone' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 

        }



class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model =ShippingAddress
        fields = [
            'user',
            'first_name',
            'last_name',
            'address',
            'city',
            'zipcode',
            'country',
            'phone',]

        widgets = {
            'user' : forms.Select(attrs={
                'class' : 'form-control'
            }), 
            'first-name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'address' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'city' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'zipcode' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'country' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 
            'phone' : forms.TextInput(attrs={
                'class' : 'form-control'
            }), 

        }