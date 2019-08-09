from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('done/', CreateDoneUserView.as_view(), name='done'),
    path('createTeacher/', CreateTeacherView.as_view(), name='teacher'),
    path('createStudent/', CreateStudentView.as_view(), name='student'),
    path('edit/<int:pk>', UpdateUserView.as_view(), name='edit'),
    path('<int:pk>/', TeacherDetailView.as_view(), name='teacher_datail'),
]
