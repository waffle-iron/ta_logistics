from django.db import models

# the following lines added:
import datetime
from django.utils import timezone


class Applications(models.Model):
    applying_class = models.CharField(max_length=6)
    ubit_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gpa = models.FloatField()
    class_grade = models.CharField(max_length=2)
    resume_url = models.URLField()

class OpenClasses(models.Model):
    class_identifier = models.CharField(max_length=6)
    professor_ubit = models.CharField(max_length=10)
    professor_first_name = models.CharField(max_length=30)
    professor_last_name = models.CharField(max_length=30)
    available_slots = models.IntegerField()


