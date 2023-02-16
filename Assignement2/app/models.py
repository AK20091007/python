from django.db import models

class classes(models.Model):
    classe_id = models.IntegerField(verbose_name="classe_id")
    classe_title = models.CharField(verbose_name="classe_title",max_length=200)
    classe_instructor = models.CharField(verbose_name="classe_instructor", max_length=200)
    classe_capacity = models.IntegerField(verbose_name="classe_capacity")
    classe_openseats = models.IntegerField(verbose_name="classe_openseats")
