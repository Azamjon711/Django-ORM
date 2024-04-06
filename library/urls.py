from django.urls import path
from .views import BookListView, BookDetailsView

urlpatterns = [
    path("library/", BookListView.as_view(), name="library"),
    path("<int:id>/book-details/", BookDetailsView.as_view(), name="book-details"),
]
