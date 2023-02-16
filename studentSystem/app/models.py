from django.db import models

class course(models.Model):
    courseid = models.IntegerField(verbose_name="courseid")
    coursetitle = models.CharField(verbose_name="coursetitle", max_length=250)
    courseinstructor = models.CharField(verbose_name="courseinstructor",max_length=250)
    coursecapacity = models.IntegerField(verbose_name="coursecapacity")
    courseopenSeats = models.IntegerField(verbose_name="courseopenSeats")
