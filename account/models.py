from distutils.command.upload import upload 
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    GENDER = (
        ('women', 'Women'),
        ('men', 'Men'),
    )
    gender = models.CharField(choices=GENDER, max_length=40)
    email = models.EmailField(('email address'), blank=True, unique=True)
    bio = models.TextField(max_length=255, blank=True)
    image = models.ImageField('Image', upload_to='user_images/')
    number = models.TextField(max_length=255, blank=True)
    birthday = models.DateField(max_length=255, null=True, blank=True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.username

    @property
    def profile_picture(self):
        if self.image:
            return self.image

    
