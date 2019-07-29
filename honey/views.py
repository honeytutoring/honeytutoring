from django.shortcuts import render, redirect
from .forms import CostomizedAutenticationForm
from django.utils.http import is_safe_url
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


class HomeView(LoginView):
    template_name = 'home.html'
    form_class = CostomizedAutenticationForm


class SignInView(FormView):
    template_name = 'signin.html'
    form_class = CostomizedAutenticationForm
    success_url = reverse_lazy('home')


class SignOutView(LogoutView):
    template_name = 'accounts/signout.html'

