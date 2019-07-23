from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import Users


class CostomizedAutenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user_qs = Users.objects.filter(username=username)
        if user_qs.count() == 0:
            raise forms.ValidationError("The user does not exist")
        else:
            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError("Incorrect password")
                if not user.is_active:
                    raise forms.ValidationError("This user is no longer active")
        return super(CostomizedAutenticationForm, self).clean()
