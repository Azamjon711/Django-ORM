from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=50, verbose_name="Address nomi")

    def __str__(self):
        return self.name


class Role(models.TextChoices):
    bachelor = ("b", "B")
    master = ("m", "M")
    phd = ("phd", "PhD")


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ism")
    last_name = models.CharField(max_length=50, verbose_name="Familiya")
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="Yoshi")
    status = models.CharField(max_length=30, choices=Role.choices, default=Role.bachelor, verbose_name="Status")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name="Address")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

