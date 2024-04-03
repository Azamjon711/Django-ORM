from django.shortcuts import render


def studentPage(request):
    return render(request, "student.html")
