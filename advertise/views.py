from django.shortcuts import render
from django.db.models import Q
from django.db.models.query import QuerySet
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .forms import UploadFileForm, PostSearchForm
from .models import Post
from django.urls import reverse_lazy
# Create your views here.


class AdvertiseIndexView(ListView):
    template_name = 'advertise/advertise_home.html'
    model = Post


class AdvertiseSearchFormView(FormView):
    template_name = 'advertise/advertise_search.html'
    form_class = PostSearchForm

    def form_valid(self, form):
        schWord = '{}'.format(self.request.POST.get('search_word'))
        post_list = Post.objects.filter(Q(content__icontains=schWord)
                                        |Q(title__icontains=schWord)
                                        |Q(region__area__icontains=schWord)
                                        |Q(subject__subject_title__icontains=schWord))
        context = {
            'form': form,
            'search_term': schWord,
            'object_list': post_list    
            }

        return render(self.request, self.template_name, context)


class AdvertiseRegionIndexView(ListView):
    template_name = 'advertise/advertise_home.html'
    model = Post

    # def get_queryset(self):
    #     filter_word =
    #     if self.model is not None:
    #         queryset = self.model.objects.filter(region__area__icontains=filter_word)
    #     else:
    #         raise ImproperlyConfigured(
    #             "%(cls)s is missing a QuerySet. Define "
    #             "%(cls)s.model, %(cls)s.queryset, or override "
    #             "%(cls)s.get_queryset()." % {
    #                 'cls': self.__class__.__name__
    #             }
    #         )
    #     ordering = self.get_ordering()
    #     if ordering:
    #         if isinstance(ordering, str):
    #             ordering = (ordering,)
    #         queryset = queryset.order_by(*ordering)
    #
    #     return queryset


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


class AdvertiseDetailView(DetailView):
    model = Post
    template_name = 'advertise/post_detail.html'


class AdvertiseCreateView(CreateView):
    template_name = 'advertise/post_form.html'
    form_class = UploadFileForm
    model = Post
    success_url = reverse_lazy('advertise:index')


class AdvertiseUpdateView(UpdateView):
    model = Post
    template_name = 'advertise/post_update.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('advertise:index')


class AdvertiseDeleteView(DeleteView):
    template_name = 'advertise/post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('advertise:index')
