from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, TemplateView
from .forms import ClassCreateForm
from .models import *
from accounts.models import Users


class ManagementIndexView(ListView):
    template_name = 'management/folder_index.html'
    model = Class

    def get_queryset(self):
        queryset = super(ManagementIndexView, self).get_queryset()
        teacher_classes = self.request.user.teacher.classes
        return teacher_classes


class ManagementDetailView(DeleteView):
    template_name = 'management/folder_detail.html'
    model = Class


class FolderCreateView(CreateView):
    template_name = 'management/folder_create.html'
    form_class = ClassCreateForm
    success_url = reverse_lazy('management:index')

    def get_form_kwargs(self):
        kwargs = super(FolderCreateView, self).get_form_kwargs()
        kwargs['class_teacher'] = self.request.user.teacher
        return kwargs


def IdCheckView(request, *args, **kwargs):
    if request.method == 'POST':
        checkid = request.POST.get('student_id')
        user_instance = Users.objects.filter(checkid)
        if user_instance.count() > 0:
            return render(request, 'management/alert.html', {'msg': '인증이 완료되었습니다.'})

        else:
            return render(request, 'management/alert.html', {'msg': '학생의 id를 다시확인하여주세요'} )
    return render(request, 'management/alert.html', {'msg': '잘못된접근입니다.'})
