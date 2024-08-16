from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from accounts.forms import RegistrationForm

# Create your views here.
class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"