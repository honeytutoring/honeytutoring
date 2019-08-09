from django.urls import path
from advertise.views import *

app_name = "advertise"

urlpatterns = [
    path('', AdvertiseIndexView.as_view(), name='index'),
    path('search/', AdvertiseSearchFormView.as_view(), name='search'),
    path('<int:pk>/', AdvertiseDetailView.as_view(), name='detail'),
    path('create/', AdvertiseCreateView.as_view(), name='create'),
    path('<int:pk>/update/', AdvertiseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AdvertiseDelete, name='delete'),
    path('condition/', ClassifiedIndexView.as_view(), name='classified')
]