from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'quantity',
            'image',
            'sizes',
            'colors',
        )