from django.urls import path
from .views import *

app_name = 'notice'

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_index'),
    path('board/answer/<int:pk>',AnswerRegisterView.as_view(), name = 'answer_register'),
    path('board/', QuestionView.as_view(), name='question_register'),
    path('board/<int:pk>/edit', QuestionEditView.as_view(), name='question_edit'),
    path('board/<int:pk>/delete', QuestionDeleteView.as_view(), name='question_delete'),

]