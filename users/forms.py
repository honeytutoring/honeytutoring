from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    group =

    class Meta:
        model = User
        fields = (
            "username",
            "fi"
            "email",
            "password1",
            "password2",
            "groups",

        )

        def save(self, commit=True):
            user = super(CreateUserForm, self).save(commit=True)

            user.email = self.clean_data

