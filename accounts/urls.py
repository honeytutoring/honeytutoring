from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('done/', CreateDoneUserView.as_view(), name='done'),
    path('edit/<int:pk>', UpdateUserView.as_view(), name='edit'),
    #path('update/', AccountUpdateView.as_view(), name='account_update'),
]
