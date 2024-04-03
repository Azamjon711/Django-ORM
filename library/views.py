from django.shortcuts import render


def libraryPage(request):
    return render(request, "library.html")
