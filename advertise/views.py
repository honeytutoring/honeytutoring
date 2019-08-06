from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from accounts.models import Users
from region.models import Region
from .forms import UploadFileForm, PostSearchForm
from .models import Post


class AdvertiseIndexView(ListView):
    template_name = 'advertise/advertise_home.html'
    model = Post

    def get(self, request, *args, **kwargs):
        return super(AdvertiseIndexView, self).get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AdvertiseIndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['user_sex_option'] = Users.GENDER_OPTION
        context['regions'] = Region.objects.all()

        return context


class AdvertiseSearchFormView(FormView):
    template_name = 'advertise/advertise_search.html'
    form_class = PostSearchForm

    def form_valid(self, form):
        schWord = '{}'.format(self.request.POST.get('search_word'))
        post_list = Post.objects.filter(Q(content__icontains=schWord)
                                        |Q(title__icontains=schWord)
                                        |Q(region__area__icontains=schWord)
                                        |Q(subject__subject_title__icontains=schWord))
        # Post.objects.filter(region__in=[1,2,3,4])

        context = {
            'form': form,
            'search_term': schWord,
            'object_list': post_list    
            }

        return render(self.request, self.template_name, context)


class ClassifiedIndexView(ListView):
    template_name = 'advertise/advertise_home.html'
    model = Post

    def get_queryset(self):
        sex = self.request.GET.get('sex')
        region = self.request.GET.get('region')
        queryset = super(ClassifiedIndexView, self).get_queryset()
        return queryset.filter(sex=sex, region=region)


class AdvertiseDetailView(DetailView):
    model = Post
    template_name = 'advertise/post_detail.html'


class AdvertiseCreateView(CreateView):
    template_name = 'advertise/post_form.html'
    form_class = UploadFileForm
    model = Post
    success_url = reverse_lazy('advertise:index')

    def get_form_kwargs(self):
        kwargs = super(AdvertiseCreateView, self).get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs


class AdvertiseUpdateView(UpdateView):
    model = Post
    template_name = 'advertise/post_update.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('advertise:index')


class AdvertiseDeleteView(DeleteView):
    template_name = 'advertise/post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('advertise:index')
