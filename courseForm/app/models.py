from django.db import models

class course(models.Model):
    course_id = models.IntegerField(verbose_name="course_id")
    course_title = models.CharField(verbose_name="course_title",max_length=300)
    course_instructor = models.CharField(verbose_name="course_instructor", max_length=300)
    course_capacity = models.IntegerField(verbose_name="course_capacity")
    course_openseats = models.IntegerField(verbose_name="course_openseats")
