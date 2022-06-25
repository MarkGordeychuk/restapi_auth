from django.urls import path
from knox.views import LogoutView

from .views import LoginView, RegisterView, UserView


urlpatterns = [
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('user', UserView.as_view(), name='user'),
]
