from django.urls import path
from advertise.views import *

app_name = "advertise"

urlpatterns = [
    path('', AdvertiseIndexView.as_view(), name='index'),
    path('search/', AdvertiseSearchFormView.as_view(), name='search'),
    path('<int:pk>/', AdvertiseDetailView.as_view(), name='detail'),
    path('create/', AdvertiseCreateView.as_view(), name='create'),
    path('<int:pk>/update/', AdvertiseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AdvertiseDeleteView.as_view(), name='delete'),
    path('subject/<int:subject_id>/', SubjectListView.as_view(), name='subject'),
    path('region/<int:region_id>/', AdvertiseRegionIndexView.as_view(), name='region'),
]