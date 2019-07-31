from django.urls import path
from .views import *

app_name = 'notice'

urlpatterns = [
    path('index/', NoticeIndexView.as_view(), name='post_index'),
    path('index/<int:pk>/', NoticeDetailView.as_view(), name='post_detail'),
    path('create/', NoticeCreateView.as_view(), name='post_create'),
    path('index/<int:pk>/update', NoticeUpdateView.as_view(), name='post_update'),
    path('index/<int:pk>/delete', NoticeDeleteView.as_view(), name='post_delete'),
]