from aifc import Error
from django.urls import URLPattern
from django.urls import path

from core.views import about,index, error404, ContactView, SubscribeView

urlpatterns = [
    
    path('about/', about, name='about'),
    path('error404/', error404, name='error404'),
    path('', index, name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),

]