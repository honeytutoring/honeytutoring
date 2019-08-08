from .forms import CostomizedAutenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CostomizedAutenticationForm


class HomeView(LoginView):
    template_name = 'home.html'
    form_class = CostomizedAutenticationForm


class SignInView(FormView):
    template_name = 'signin.html'
    form_class = CostomizedAutenticationForm
    success_url = reverse_lazy('home')


class SignOutView(LogoutView):
    template_name = 'accounts/signout.html'
