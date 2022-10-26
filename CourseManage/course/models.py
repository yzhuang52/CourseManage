from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    credit = models.IntegerField(verbose_name="credit")
