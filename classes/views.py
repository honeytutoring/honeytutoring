from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib import messages
from accounts.models import User
from .forms import *
from .models import *
from pure_pagination.mixins import PaginationMixin


class ClassesListView(PaginationMixin, ListView):
    template_name = 'classes/class_list.html'
    model = Class
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ClassesListView, self).get_queryset()
        if User.USER_TEACHER == self.request.user.user_type:
            teacher_classes = self.request.user.teacher.classes.all()
            return teacher_classes
        elif User.USER_STUDENT == self.request.user.user_type:
            student_classes = self.request.user.student.classes.all()
            return student_classes
        # elif Users.USER_PARENT == self.request.user.user_type:
        #     retu


class ClassDetailView(DetailView):
    template_name = 'classes/class_detail.html'
    model = Class
    pk_url_kwarg = 'class_id'

    def get_context_data(self, **kwargs):
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        context['memo_list'] = self.object.memo
        return context


class ScheduleCreateView(CreateView):
    template_name = 'classes/class_detail.html'
    model = Schedule
    pk_url_kwarg = 'class_id'
    form_class = ScheduleCreateForm

    def get_success_url(self):
        class_id = self.kwargs.get('class_id')
        return reverse_lazy('classes:detail', kwargs={'class_id': class_id})

    def get(self, request, *args, **kwargs):
        raise Http404

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, '올바르지 않은 스케줄입니다.')
        return HttpResponse(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super(ScheduleCreateView, self).get_form_kwargs()
        kwargs['klass_id'] = self.kwargs.get('class_id')
        return kwargs


class MemoCreateView(CreateView):
    template_name = 'classes/class_detail.html'
    model = Memo
    form_class = MemoCreateForm
    pk_url_kwarg = 'class_id'

    def post(self, request, *args, **kwargs):
        return super(MemoCreateView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        class_id = self.kwargs.get('class_id')
        return reverse_lazy('classes:detail', kwargs={'class_id': class_id})

    def get(self, request, *args, **kwargs):
        raise Http404

    def get_form_kwargs(self):
        kwargs = super(MemoCreateView, self).get_form_kwargs()
        kwargs['klass_id'] = self.kwargs.get('class_id')
        return kwargs


class ClassCreateView(CreateView):
    template_name = 'classes/class_create.html'
    form_class = ClassCreateForm
    success_url = reverse_lazy('classes:index')

    def get_form_kwargs(self):
        kwargs = super(ClassCreateView, self).get_form_kwargs()
        kwargs['class_teacher'] = self.request.user.teacher
        return kwargs

    def form_valid(self, form):
        self.object = form.save()

        students = self.request.POST.getlist('students')
        students = list(filter(lambda x: x, students))

        self.object.students.add(*students)

        return HttpResponseRedirect(self.get_success_url())


class ClassDeleteView(DeleteView):
    pass


class ScheduleDeleteView(DeleteView):
    template_name = 'classes/class_detail.html'
    model = Schedule
    pk_url_kwarg = 'schedule_id'

    def get_success_url(self):
        class_id = self.kwargs.get('class_id')
        return reverse_lazy('classes:detail', kwargs={'class_id': class_id})

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class MemoDeleteView(DeleteView):
    template_name = 'classes/class_detail.html'
    model = Memo
    pk_url_kwarg = 'memo_id'


@csrf_exempt
def StudentIdCheck(request, *args, **kwargs):
    user_name = request.GET.get('name')
    student_user = get_object_or_404(User, username=user_name)

    if hasattr(student_user, 'student'):
        return JsonResponse({'student_id': student_user.student.id})
    raise Http404
