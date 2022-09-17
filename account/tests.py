from django.test import TestCase
import account
from account.models import User
from account.models import Myaccount
from account.models import Myinformation
from account.models import Myfirstadress
from account.models import Mycreditslips



class TestaccountModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'name' : 'Aynur',
            'email' : 'aynursafarova02@gmail.com', 
            'phone' : '0774171824',
            'password' : '12345',
            'my_account' : 'aynurrr'
        }
        cls.User = User.objects.create(**cls.data1)
    def test_created_data(self):
        user = User.objects.first()
        self.assertEqual(user.name, self.data1['name']),
        self.assertEqual(user.email, self.data1['email']),
        self.assertEqual(user.phone, self.data1['phone']),
        self.assertEqual(user.password, self.data1['password']),
        self.assertEqual(user.my_account, self.data1['my_account'])

    def test_str_method(self):
        self.assertEqual(str(self.User),self.data1["name"])


        @classmethod
        def tearDownClass(cls):
            User.objects.first().delete()
            del cls.data1

