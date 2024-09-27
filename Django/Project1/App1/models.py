from django.db import models

# Create your models here.
class Line(models.Model):
    line_name = models.CharField(max_length=100)

    def __str__(self):
        return self.line_name

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_line = models.ManyToManyField(Line)

    def __str__(self):
        return self.station_name