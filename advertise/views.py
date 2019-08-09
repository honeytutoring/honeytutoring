from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
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


class ClassifiedIndexView(View):
    template_name = 'advertise/advertise_home.html'
    model = Post
    # context_object_name = 'filter_list'

    def post(self, form):
        query = "ok"
        author = self.request.POST.get('name')
        subject = self.request.POST.get('subject')
        region = self.request.POST.get('region_1')
        classified_region_name = self.request.POST.get('region_2')
        sex = self.request.POST.getlist('sex')
        name = list(author)
        query_name1 = "".join(name[1:])
        query_name2 = "".join(name[2:])
        # queryset = super(ClassifiedIndexView, self).get_queryset()
        
        #qlist = [author, subject, region, classified_region_name]
        # if len(sex) == 2 or len(sex)==0 :
        #     obj = Post.objects.all()
        # for i in qlist:
        #     if (qlist[i] == "선생님 이름") or (qlist[i] == "선택 없음"):
        #         qlist.remove(qlist[i])
        if author == '':
            if subject == "선택 없음":
                if region == "선택 없음":
                    context = Post.objects.all()
                elif classified_region_name == "선택 없음":
                    context = Post.objects.filter(region__area=region)
                else:
                    context = Post.objects.filter(region__area=region, classifiedregion__classified_region =classified_region_name)
            elif region == "선택 없음":
                context = Post.objects.filter(subject__subject_title=subject)
            elif classified_region_name == "선택 없음":
                context = Post.objects.filter(subject__subject_title=subject, region__area=region)
            else:
                context = Post.objects.filter(subject__subject_title=subject, region__area=region, classifiedregion__classified_region =classified_region_name)
        
        elif query_name1 == '':
            context = None

        else:
        
            if subject == "선택 없음":
                if region == "선택 없음":
                    context = Post.objects.filter(Q(author__first_name__icontains=query_name1) or Q(author__first_name__icontains=query_name2))
                elif classified_region_name == "선택 없음":
                    context = Post.objects.filter(Q(author__first_name__icontains=query_name1) or Q(author__first_name__icontains=query_name2) ,region__area=region)
                else:
                    context = Post.objects.filter(Q(author__first_name__icontains=query_name1) or Q(author__first_name__icontains=query_name2), region__area=region, classifiedregion__classified_region =classified_region_name)
            elif region == "선택 없음":
                context = Post.objects.filter(Q(author__first_name__icontains=query_name1) or Q(author__first_name__icontains=query_name2) , subject__subject_title=subject)
            elif classified_region_name == "선택 없음":
                context = Post.objects.filter(Q(author__first_name__icontains=query_name1) or Q(author__first_name__icontains=query_name2) , subject__subject_title=subject, region__area=region)
            else:
                context = Post.objects.filter(Q(author__first_name__icontains=query_name1) or Q(author__first_name__icontains=query_name2) , subject__subject_title=subject, region__area=region, classifiedregion__classified_region =classified_region_name)


        if len(sex) == 2 or len(sex) == 0:
            context = {'context': context,
                        'regions': Region.objects.all(),
                        'object_list': Post.objects.all(),
                        'query': query
            }
            return render(self.request, self.template_name, context)        
        else:
            if sex[0] == "여성":
                context = context.filter(author__sex=1)
                context = {'context': context,
                'regions': Region.objects.all(),
                'object_list': Post.objects.all(),
                'query':query
            }
                return render(self.request, self.template_name, context)
            elif sex[0] == "남성":
                context = context.filter(author__sex=0)
                context = {'context': context,
                'regions': Region.objects.all(),
                'object_list': Post.objects.all(),
                'query':query
            }
                return render(self.request, self.template_name, context)


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
