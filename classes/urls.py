from django.urls import path
from .views import *

app_name = 'classes'

urlpatterns = [
     path('', ClassesListView.as_view(), name='index'),
     path('<int:class_id>', ClassDetailView.as_view(), name='detail'),
     path('create/', ClassCreateView.as_view(), name='create'),
     path('studentcheck/', StudentIdCheck, name='student_check'),
     path('<int:class_id>/schedules/create/', ScheduleCreateView.as_view(), name='schedule_create'),
     path('<int:class_id>/memo/create/', MemoCreateView.as_view(), name='memo_create'),
     path('<int:class_id>/delete/', ClassDeleteView.as_view(), name='delete'),
     path('<int:class_id>/schedules/<int:schedule_id>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),
     path('<int:class_id>/memo/<int:memo_id>/delete/', MemoDeleteView.as_view(), name='memo_delete'),
]
