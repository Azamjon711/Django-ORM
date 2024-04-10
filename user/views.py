from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class UserRegisterView(View):
    def get(self, request):
        return render(request, "user/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password_1"]
        confirm_password = request.POST["password_2"]

        if password == confirm_password:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            checkUser = User.objects.filter(username=username, password=password)
            if checkUser:
                return render(request, "user/register.html")
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password)
                user.save()
                return redirect("login")
        else:
            return render(request, "user/register.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "user/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }

        loginForm = AuthenticationForm(data=data)

        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect("main")
        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, "user/login.html")


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("main")
