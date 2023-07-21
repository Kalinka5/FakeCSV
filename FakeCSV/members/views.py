from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import ProfileForm, PasswordChangingForm


class UserRegisterView(View):
    template_name = "registration/register.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        username = self.request.POST.get("username")
        email = self.request.POST.get("email")
        password = self.request.POST.get("password")
        conf_password = self.request.POST.get("conf-password")
        password_mismatch = False

        if password != conf_password:
            password_mismatch = True
        else:
            usr = User.objects.create_user(username, email, password)
            usr.save()
            return redirect("login")
        
        register = {"password_mismatch": password_mismatch, "username": username, "email": email}
        
        return render(self.request, self.template_name, register)
        

class UserProfileView(generic.UpdateView):
    form_class = ProfileForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy('data_schemas')

    def get_object(self):
        return self.request.user
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})
