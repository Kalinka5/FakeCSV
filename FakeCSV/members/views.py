from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User


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
        
