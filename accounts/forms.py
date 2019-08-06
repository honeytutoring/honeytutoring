from django.contrib.auth import authenticate

from accounts.models import Users, Teacher, Student
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Users
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'sex',
            'user_type',
        )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(CreateUserForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        ret = super(CreateUserForm, self).save(commit)
        if commit:
            self.user = authenticate(
                self.request,
                username=self.cleaned_data.get('username'),
                password=self.cleaned_data.get('password2')
            )

        return ret


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ('user',)
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(TeacherForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.user
        return super(TeacherForm, self).save(commit=commit)


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ('user',)
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(StudentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.user
        return super(StudentForm, self).save(commit=commit)
