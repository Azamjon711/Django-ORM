from django.urls import path
from .views import StudentListView, StudentDetailsView

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student"),
    path("<int:id>/student-details/", StudentDetailsView.as_view(), name="student-details"),
]
