from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class NoticeIndexView(ListView):
    template_name = 'notice/notice_index.html'
    model = Posts
    paginate_by = 10
    context_object_name = 'posts'
    ordering = ['-create_date', ]

    def get_ordering(self):
        return self.ordering


class NoticeDetailView(DetailView):
    template_name = 'notice/notice_detail.html'
    model = Posts


class NoticeCreateView(SuccessMessageMixin, CreateView):
    template_name = 'notice/notice_writing.html'
    success_message = "article was created successfully"
    model = Posts
    form_class = PostForm
    success_url = reverse_lazy('notice:post_index')


class NoticeUpdateView(SuccessMessageMixin, UpdateView):
    success_message = "Article was update successfully"
    model = Posts
    form_class = PostForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('notice:post_index')


class NoticeDeleteView(SuccessMessageMixin, DeleteView):
    template_name_suffix = '_delete'
    model = Posts
    success_message = "%(name)s was deleted successfully"
    success_url = reverse_lazy('notice:post_index')
