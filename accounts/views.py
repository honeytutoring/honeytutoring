from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import CreateUserForm, TeacherForm, StudentForm
from .models import Users
from django.contrib.auth import login as auth_login


class CreateUserView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CreateUserForm

    def get_form_kwargs(self):
        kwargs = super(CreateUserView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        return super(CreateUserView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CreateUserView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        user_type = self.request.POST.get('user_type')
        if user_type == str(Users.USER_TEACHER):
            return reverse_lazy('accounts:teacher')
        elif user_type == str(Users.USER_STUDENT):
            return reverse_lazy('accounts:student')

    def form_valid(self, form):
        ret = super(CreateUserView, self).form_valid(form)
        auth_login(self.request, form.user)
        return ret


class CreateDoneUserView(TemplateView):
    template_name = 'accounts/signup_done.html'


class UpdateUserView(UpdateView):
    template_name = 'accounts/account_update.html'
    form_class = CreateUserForm
    model = Users
    success_url = reverse_lazy('home')


class CreateTeacherView(CreateView):
    template_name = 'accounts/create_teacher.html'
    form_class = TeacherForm
    success_url = reverse_lazy('accounts:done')

    def get_form_kwargs(self):
        kwargs = super(CreateTeacherView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateStudentView(CreateView):
    template_name = 'accounts/create_student.html'
    form_class = StudentForm
    success_url = reverse_lazy('accounts:done')

    def get_form_kwargs(self):
        kwargs = super(CreateStudentView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TeacherDetailView(DetailView):
    template_name = 'accounts/teacher_datail.html'
    model = Users
    context_object_name = 'user'
