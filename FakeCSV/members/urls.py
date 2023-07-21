from django.urls import path
from .views import UserRegisterView, UserProfileView, PasswordsChangeView, password_success

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', password_success, name='password_success')
]
