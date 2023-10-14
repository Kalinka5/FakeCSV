from django.urls import path
from .views import (
    UserRegisterView,
    UserProfileView,
    update_user,
    DeleteUserView,
    PasswordsChangeView,
    password_success)

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit', update_user, name='edit_profile'),
    path('profile/delete', DeleteUserView.as_view(), name='account_delete'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password-success/', password_success, name='password_success'),
    path('password-reset/', 
        PasswordResetView.as_view(
            template_name='registration/password_reset.html',
            html_email_template_name='registration/password_reset_email.html'), 
        name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]
