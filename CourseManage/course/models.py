from django.db import models
from django.contrib import admin


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    credit = models.IntegerField(verbose_name="credit")
    student = models.CharField(max_length=50, verbose_name="student", default="student")

    def __str__(self):
        return self.name
