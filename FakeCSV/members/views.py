from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages

from .forms import NewUserForm, ProfileForm, PasswordChangingForm


class UserRegisterView(CreateView):
    template_name = "registration/register.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        password_mismatch = False
        form = NewUserForm(self.request.POST)
        username = self.request.POST.get("username")
        email = self.request.POST.get("email")
        if form.is_valid():
            form.save()
            messages.success(self.request, "Registration successful." )
            return redirect("login")
        else:
            password_mismatch = True
        
        register = {"password_mismatch": password_mismatch, "username": username, "email": email}
        
        return render(self.request, self.template_name, register)
        

class UserProfileView(UpdateView):
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
