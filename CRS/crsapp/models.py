from django.db import models

class Stream(models.Model):
    Streamid = models.IntegerField(verbose_name="StreamID")
    Streamtitle = models.CharField(verbose_name="StreamTitle", max_length=230)
    Streaminstructor = models.CharField(verbose_name="StreamInstructor",max_length=170)
    Streamcapacity = models.IntegerField(verbose_name="StreamCapacity")
    StreamopenSeats = models.IntegerField(verbose_name="StreamOpenseats")
