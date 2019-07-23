from django.shortcuts import render,HttpResponseRedirect, reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.urls import reverse_lazy


class CreateUserView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accounts:done')


class CreateDoneUserView(CreateView):
    template_name = 'accounts/signup_done.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accounts:done')


class PasswordResetView(TemplateView):
    pass


