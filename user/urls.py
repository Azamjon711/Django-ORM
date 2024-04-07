from django.urls import path
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path("user/register/", UserRegisterView.as_view(), name="register"),
    path("user/login/", UserLoginView.as_view(), name="login"),

]
