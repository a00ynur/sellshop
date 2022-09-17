from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=40)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(_("Email"), unique = True, max_length=40)
    is_active = models.BooleanField("Is active", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email