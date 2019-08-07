from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView, CreateView, FormView, UpdateView, DeleteView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class QuestionView(SuccessMessageMixin, CreateView):
    template_name = 'question/q_a_register.html'
    success_message = "Question was successfully registered!"
    model = QandA
    form_class = QuestionForm
    success_url = reverse_lazy('question:question_index')

class QuestionListView(ListView):
    template_name = 'question/q_a_list.html'
    model = QandA
    paginate_by = 10
 


class AnswerRegisterView(View):
    
    def post(self,form,**kwargs):
        answer_edit = self.request.POST.get('answer')
        target = QandA.objects.filter(pk=self.kwargs['pk'])
        target.update(answer = answer_edit)
        target.update(answer_registered='답변완료')

        return HttpResponseRedirect(reverse_lazy('question:question_index'))

    
class QuestionEditView(SuccessMessageMixin, UpdateView):
    success_message = "Question was successfully edited"
    template_name = 'question/q_a_update.html'
    model = QandA
    form_class = QuestionForm
    success_url = reverse_lazy('question:question_index')

class QuestionDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'question/q_a_delete.html'
    model = QandA
    success_message = "%(name)s was deleted successfully"
    success_url = reverse_lazy('quesiton:question_index')
