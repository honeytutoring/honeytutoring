from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


class NoticeIndexView(ListView):
    template_name = 'notice/notice_index.html'
    model = Posts
    paginate_by = 10
    context_object_name = 'posts'


class NoticeDetailView(DetailView):
    template_name = 'notice/notice_detail.html'
    model = Posts


class NoticeRedirectView(CreateView):
    model = Posts
    form_class = PostForm
    success_url = reverse_lazy('notice:post_index')


class NoticeWritingView(FormView):
    template_name = 'notice/notice_writing.html'
    form_class = PostForm


class NoticeUpdateView(UpdateView):
    pass


class NoticeDelteView(DeleteView):
    pass

