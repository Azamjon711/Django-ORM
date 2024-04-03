from django.db import models
from student.models import Student


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    text = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Comment)
    create_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.title} {self.price}"


class BookingBook(models.Model):
    student = models.ManyToManyField(Student)
    book = models.ManyToManyField(Book)
    get_date = models.DateTimeField(auto_now_add=True)
    return_date = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} {self.book}"


