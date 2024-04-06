from django.shortcuts import render
from django.views import View


# def mainPage(request):
#     return render(request, "mainPage.html")

class MainView(View):
    def get(self, request):
        return render(request, "mainPage.html")


