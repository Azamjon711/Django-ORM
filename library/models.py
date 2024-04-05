from django.db import models
from student.models import Student


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ism")
    last_name = models.CharField(max_length=50, verbose_name="Familiya")
    birth_date = models.DateField(auto_now_add=True, verbose_name="Tug'ilgan yil")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    text = models.TextField(verbose_name="Matn")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student ism")

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Kitob nomi")
    description = models.TextField(verbose_name="Tavsif")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    count = models.IntegerField(default=1, verbose_name="Soni")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Avtor ismi")
    comment = models.ManyToManyField(Comment, verbose_name="Komment")
    create_date = models.DateTimeField(auto_created=True, verbose_name="Yaratilgan sana")

    def __str__(self):
        return f"{self.title} {self.price}"


class BookingBook(models.Model):
    student = models.ManyToManyField(Student, verbose_name="Student ismi")
    book = models.ManyToManyField(Book, verbose_name="Kitob nomi")
    get_date = models.DateTimeField(auto_now_add=True, verbose_name="Olingan vaqti")
    return_date = models.BooleanField(default=False, verbose_name="Qaytarilganmi?")

    def __str__(self):
        return f"{self.student} {self.book}"


