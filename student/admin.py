from django.contrib import admin
from .models import Student, Address
from import_export.admin import ImportExportModelAdmin


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ("first_name", "last_name", "age", "status", "address")
    list_display_links = ("first_name", "last_name", "age", "address")
    search_fields = ("first_name", "last_name", "address")
    ordering = ("age",)
    list_filter = ("first_name", "last_name", "age", "status", "address")
    list_editable = ("status",)


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    # list_display_links = ("name", )
    # search_fields = ("name", )
    # ordering = ("name", )
    # list_filter = ("name", )
