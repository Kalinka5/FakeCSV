from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .forms import NewUserForm, ProfileForm, ProfileImgForm, PasswordChangingForm
from CSV_converter.models import Profile


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
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
    def post(self, *args, **kwargs):
        current_user = get_object_or_404(User, id=self.request.user.id)
        profile_user, created = Profile.objects.get_or_create(user=current_user)
        profile_img_form = ProfileImgForm(self.request.POST or None, self.request.FILES or None, instance=profile_user)
        if profile_img_form.is_valid():
            profile_img_form.save()
            return redirect('profile')
    

def update_user(request):
    if request.user.is_authenticated:
        current_user = get_object_or_404(User, id=request.user.id)
        # Get forms
        user_form = ProfileForm(request.POST or None, request.FILES or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, ("Your Profile has been updated"))
            return redirect('profile')
        
        return render(request, "registration/update_user.html", {'user_form': user_form})
    else:
        messages.success(request, ("You must be logged in to view that page..."))
        return redirect('profile')


class DeleteUserView(DeleteView):
    model = User
    template_name = "registration/delete_account.html"
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})
