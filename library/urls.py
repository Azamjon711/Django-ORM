from django.urls import path
from .views import libraryPage

urlpatterns = [
    path("library/", libraryPage),
]
