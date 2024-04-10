from django.shortcuts import render
from django.views import View
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            books = Book.objects.all()
            context = {
                "books": books,
                "search": search
            }
            return render(request, "library.html", context)
        else:
            books = Book.objects.filter(title__icontains=search)
            if books:
                context = {
                    "books": books,
                    "search": search
                }
                return render(request, "library.html", context)
            else:
                return render(request, "notFound.html")


class BookDetailsView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, "bookDetail.html", {"book": book})

