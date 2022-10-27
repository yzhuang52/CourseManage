from django.db import models
from user.models import Student


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    credit = models.IntegerField(verbose_name="credit")
    student = models.ForeignKey(Student, to_field="name", verbose_name="student", on_delete=models.CASCADE, default="student") 

    def __str__(self):
        return self.name
