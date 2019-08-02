from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('done/', CreateDoneUserView.as_view(), name='done'),
    # path('password_reset/', PasswordResetView.as_view(), name='passwordreset'),
    path('edit/<int:pk>/', UpdateUserView.as_view(), name='edit'),
]
