from django.test import TestCase
from unicodedata import name
from product.models import Product


class TestproductModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Aynur',
            'price' : '111', 
            'quantity' : '3',

        }
        cls.Product = Product.objects.create(**cls.data1)


    def test_created_data(self):
        product = Product.objects.first()
        self.assertEqual(product.title, self.data1['title'])
        self.assertEqual(product.price, self.data1['price'])
        self.assertEqual(product.quantity, self.data1['quantity'])
        

    def test_str_method(self):
        self.assertEqual(str(self.Product),self.data1["name"])
        @classmethod
        def tearDownClass(cls):
            Product.objects.first().delete()
            del cls.Product
            del cls.data1
            
            