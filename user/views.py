from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User


class UserRegisterView(View):
    def get(self, request):
        return render(request, "user/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]

        user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password_1)
        # user.set_password(password_1)
        user.save()

        return redirect("login")


class UserLoginView(View):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.filter(username=username, password=password)

        if user:
            return redirect("main")
        else:
            return render(request, "userNotFound.html")
