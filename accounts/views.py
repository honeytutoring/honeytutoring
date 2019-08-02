from django.views.generic import TemplateView, FormView, RedirectView
from django.views.generic.edit import CreateView, UpdateView
from .forms import CreateUserForm
from .models import Users
from .forms import CreateUserForm, AccountUpdateForm
from django.urls import reverse_lazy


class CreateUserView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accounts:done')


class CreateDoneUserView(TemplateView):
    template_name = 'accounts/signup_done.html'

class UpdateUserView(UpdateView):
    template_name = 'accounts/account_update.html'
    form_class = CreateUserForm
    model = Users
    success_url = reverse_lazy('home')

# class PasswordResetView(TemplateView):
#     pass


class AccountUpdateView(UpdateView):
    template_name = 'accounts/account_update.html'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accounts:account_update')

