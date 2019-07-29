from django.urls import path
from .views import *

app_name = 'notice'

urlpatterns = [
    path('index/', NoticeIndexView.as_view(), name='post_index'),
    path('detail/<int:id>/', NoticeDetailView.as_view(), name='post_detail'),
    path('writing/', NoticeWritingView.as_view(), name='post_writing'),
    path('create/', NoticeRedirectView.as_view(), name='post_create'),
]