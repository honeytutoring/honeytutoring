from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib import messages

from accounts.models import Users
from .forms import *
from .models import *


class ClassesListView(ListView):
    template_name = 'classes/class_list.html'
    model = Class

    def get_queryset(self):
        queryset = super(ClassesListView, self).get_queryset()
        teacher_classes = self.request.user.teacher.classes
        return teacher_classes


class ClassDetailView(DetailView):
    template_name = 'classes/class_detail.html'
    model = Class
    pk_url_kwarg = 'class_id'

    # def get_context_data(self, **kwargs):
    #     context = super(ManagementDetailView, self).get_context_data(**kwargs)
    #     context['schedule_list'] = self.object.schdules
    #     context['student_list'] = self.object.students
    #     return context


class ScheduleCreateView(CreateView):
    template_name = 'classes/class_detail.html'
    model = Schedule
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
    model = Memo
    success_url = reverse_lazy('classes:detail')

    def get(self, request, *args, **kwargs):
        return redirect('classes:detail')


class ClassCreateView(CreateView):
    template_name = 'classes/class_create.html'
    form_class = ClassCreateForm
    success_url = reverse_lazy('classes:index')

    def get_form_kwargs(self):
        kwargs = super(ClassCreateView, self).get_form_kwargs()
        kwargs['class_teacher'] = self.request.user.teacher
        return kwargs


class ClassDeleteView(DeleteView):
    pass


class ScheduleDeleteView(DeleteView):
    pass


class MemoDeleteView(DeleteView):
    pass



@csrf_exempt
def idCheck(request, *args, **kwargs):
        checkid = request.GET.get('name')
        user_instance = Users.objects.filter(username=checkid)
        if user_instance.count() > 0:
            context = {'msg': '인증이 완료되었습니다.'}
            return JsonResponse(context, json_dumps_params={'ensure_ascii': True})
        else:
            context = {'msg': '학생의 id를 다시확인하여주세요'}
            return JsonResponse(context, json_dumps_params={'ensure_ascii': True})

