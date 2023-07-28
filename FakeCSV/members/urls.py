from django.urls import path
from .views import UserRegisterView, UserProfileView, DeleteUserView, PasswordsChangeView, password_success

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/delete', DeleteUserView.as_view(), name='account_delete'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', password_success, name='password_success')
]
