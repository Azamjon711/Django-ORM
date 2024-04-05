from django.contrib import admin
from .models import Book, Author, BookingBook, Comment
from import_export.admin import ImportExportModelAdmin


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "description", "price", "count", "author", "create_date")
    list_display_links = ("id", "title", "description", "price", "count", "create_date")
    search_fields = ("title", "description")
    ordering = ("-create_date",)
    # filter_horizontal = ("comment", )
    list_filter = ("title", "author", "price")
    date_hierarchy = "create_date"
    list_editable = ("author", )


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("first_name", "last_name", "birth_date")
    list_display_links = ("first_name", "last_name", "birth_date")
    search_fields = ("first_name", "last_name")
    ordering = ("birth_date",)
    list_filter = ("first_name", "last_name", "birth_date")
    date_hierarchy = "birth_date"


@admin.register(BookingBook)
class BookingBookAdmin(ImportExportModelAdmin):
    list_display = ("get_date", "return_date")
    list_display_links = ("get_date",)
    ordering = ("get_date",)
    list_filter = ("student", "book")
    date_hierarchy = "get_date"
    list_editable = ("return_date",)


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ("student", "text")
    list_display_links = ("student", "text")
    search_fields = ("text",)
    ordering = ("student",)
    list_filter = ("student", "text")
