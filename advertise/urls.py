from django.urls import path
from advertise import views
app_name = "advertise"

urlpatterns = [
    path('', views.PostListView.as_view(), name='main'),
    path('search/',views.SearchListView.as_view(), name='search'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('subject/<int:subject_id>/', views.SubjectListView.as_view(), name='subject'),
    path('region/<int:region_id>/', views.RegionListView.as_view(), name='region'),
]