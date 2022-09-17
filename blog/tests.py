from unicodedata import name
from django.test import TestCase
from blog.models import Blog 


class TestblogModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'name' : 'Aynur',
            'email' : 'aynursafarova02@gmail.com', 
            'message' : 'hello world'
        }
        cls.Blog = Blog.objects.create(**cls.data1)


    def test_created_data(self):
        blog = Blog.objects.first()
        self.assertEqual(blog.name, self.data1['name'])
        self.assertEqual(blog.email, self.data1['email'])
        self.assertEqual(blog.message, self.data1['message'])
        

    def test_str_method(self):
        self.assertEqual(str(self.Blog),self.data1["name"])
        @classmethod
        def tearDownClass(cls):
            Blog.objects.first().delete()
            del cls.Blog
            del cls.data1
            
            