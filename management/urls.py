from django.urls import path
from .views import *

app_name = 'management'

urlpatterns = [
     path('index/', ManagementIndexView.as_view(), name='index'),
     path('detail/<int:pk>', ManagementDetailView.as_view(), name='detail'),
     path('create/', FolderCreateView.as_view(), name='create'),
     path('check/', IdCheckView, name='check'),
]