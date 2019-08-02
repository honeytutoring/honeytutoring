from accounts.models import Users
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Users
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'sex',
            'user_type',
        )

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

#
# class AccountUpdateForm(forms.ModelForm):
#
#     class Meta:
#         model = Users
#