from django.shortcuts import render


def mainPage(request):
    return render(request, "mainPage.html")
