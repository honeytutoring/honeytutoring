from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UploadFileForm
from .models import Post
from django.urls import reverse_lazy
# Create your views here.


class PostListView(ListView):
    template_name = 'advertise/advertise_home.html'
    model = Post


class SearchListView(ListView):
    template_name = 'advertise/advertise_search.html'
    model = Post

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class RegionListView(ListView):
    template_name = 'advertise/advertise_home.html'
    model = Post
    
    def get_queryset(self):
        query = self.kwargs['region_id']
        if query == 0:
            object_list = Post.objects.filter(region__icontains='서울')
            return object_list
        elif query == 1:
            object_list = Post.objects.filter(region__icontains='경기도')
            return object_list
        elif query ==2:
            object_list = Post.objects.filter(region__icontains='충청도')
            return object_list


class SubjectListView(ListView):
    template_name = 'advertise/advertise_home.html'
    model = Post

    def get_queryset(self):
        query = self.kwargs['subject_id']
        if query == 0:
            object_list = Post.objects.filter(subject__icontains='국어')
            return object_list
        elif query == 1:
            object_list = Post.objects.filter(subject__icontains='수학')
            return object_list
        elif query ==2:
            object_list = Post.objects.filter(subject__icontains='영어')
            return object_list


class PostDetailView(DetailView):
    model = Post
    template_name = 'advertise/post_detail.html'


class PostCreateView(CreateView):
    form_class = UploadFileForm
    model = Post
    template_name = 'advertise/post_form.html'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'advertise/post_update.html'
    form_class = UploadFileForm


class PostDeleteView(DeleteView):
    template_name = 'advertise/post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('advertise:main')
