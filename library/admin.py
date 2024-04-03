from django.contrib import admin
from .models import Book, Author, BookingBook, Comment

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookingBook)
admin.site.register(Comment)
