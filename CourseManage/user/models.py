from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    password = models.CharField(max_length=30, verbose_name="password")
    email = models.EmailField(verbose_name="email")

