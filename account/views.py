from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.views.generic import View,CreateView
from account.forms import LoginForm, RegisterForm, CustomPasswordChangeForm, UpdatePersonalInfoForm
from account.tasks import send_confirmation_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login as django_login, logout as django_logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.mixins import LoginRequiredMixin
from basket.forms import BillingAddressForm
from account.tokens import account_activation_token
from django.contrib.auth.views import PasswordChangeView
# from account.forms import PasswordChangingForm
from account.forms import (RegisterForm, ResetPasswordForm, 
        LoginForm,
        CustomSetPasswordForm, 
        )
USER = get_user_model()

class RegisterView(CreateView):

    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


@login_required
def account(request):
    form_account = BillingAddressForm
  
    form_personal_info = UpdatePersonalInfoForm()
    
    if request.method == 'POST':
        if request.POST.get('submit') == 'address':
            form_account = BillingAddressForm(data=request.POST)
            if form_account.is_valid():
                form_account.save()
            return redirect(reverse_lazy('account'))
        elif request.POST.get('submit') == 'personal_info_submit':
            form_personal_info = UpdatePersonalInfoForm(data=request.POST)
            if form_personal_info.is_valid():
                request.user.first_name = request.POST.get('first_name')
                request.user.last_name = request.POST.get('last_name')
                request.user.email = request.POST.get('email')
                request.user.birthday = request.POST.get('birthday')
                request.user.gender= request.POST.get('gender')
                request.user.save()
                return redirect(reverse_lazy('account'))
    context = {
        'form_account':form_account,
       
        'form_personal_info':form_personal_info,
    } 
    if request.user.is_authenticated:
        return render(request, "my-account.html")
    return render(request, "error-404.html")


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')


    

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'forgot-password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Sizin yeni sifreniz teyin edildi')
        return super().get_success_url()

class ResetPasswordView(PasswordResetView):
    template_name = 'forgot-password.html'
    form_class = ResetPasswordForm
    email_template_name = 'resetpassword.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        return super().get_success_url()    




class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'changepassword.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Your password has been successfully changed')
        return super().get_success_url()


class Activate(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = USER.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, USER.DoesNotExist):
            user = None
        if user.is_active:
            messages.add_message(request, messages.SUCCESS, 'Email has been confirm')
            return redirect(reverse_lazy('login'))
        elif user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Email confirmed')
            return redirect(reverse_lazy('login'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Email didnot confirm')
            return redirect(reverse_lazy('/'))
@login_required
def logout(request):
    django_logout(request)
    return redirect('/')