from django.shortcuts import render
from django.views import View
from .models import Student
from django.contrib.auth.mixins import LoginRequiredMixin


class StudentListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            students = Student.objects.all()
            context = {
                "students": students,
                "search": search
            }
            return render(request, "student.html", context)
        else:
            students = Student.objects.filter(first_name__icontains=search)
            if students:
                context = {
                    "students": students,
                    "search": search
                }
                return render(request, "student.html", context)
            else:
                return render(request, "notFound.html")


class StudentDetailsView(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        return render(request, "studentDetail.html", {"student": student})
