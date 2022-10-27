from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="name", unique=True, default="student")
    password = models.CharField(max_length=30, verbose_name="password")
    email = models.EmailField(verbose_name="email")

    def __str__(self):
        return self.name