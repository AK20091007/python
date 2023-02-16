from django.db import models

# Create your models here.

# inherit from models.Model

class Courses(models.Model):
    courseid = models.IntegerField(verbose_name="ID")
    title = models.CharField(verbose_name="Title", max_length=150)
    instructor = models.CharField(verbose_name="Instructor",max_length=150)
    capacity = models.IntegerField(verbose_name="Capacity")
    openSeats = models.IntegerField(verbose_name="Openseats")
