from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .forms import ContactForm, SubscribeForm
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from product.models import ProductVersion
from django.db.models import Count
from core.models import Contact

def about(request):
    return render(request,'about.html')

def error404(request):
    return render(request,'error-404.html')

def index(request):
     return render(request,'index.html')


class SubscribeView(CreateView):
    template_name = 'index.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        context = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Email received')
        return context



def contact(request):
    form = ContactForm()
    print(request.POST)
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('error'))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
class ContactView(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = '__all__'
    success_url = reverse_lazy('contact')
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Your message is accepted!')
        return super().get_success_url()