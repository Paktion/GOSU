from django.db import models


class Bus_Stop(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
