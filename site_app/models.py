"""
Module from django.db to import models
"""
from django.db import models


class Weather(models.Model):
    """
    Table for Weather list
    """
    date = models.DateField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    precipitation = models.FloatField()
    station_id = models.CharField(max_length=20)


class Yield(models.Model):
    """
    Table for Crop Yield list
    """
    total_corn = models.IntegerField()
    year = models.IntegerField()


class Results(models.Model):
    """
    Table for Data Analysis of Weather table results
    """
    year = models.IntegerField(default=2022)
    station_id = models.CharField(max_length=20, default="")
    avg_max_temperature = models.FloatField()
    avg_min_temperature = models.FloatField()
    total_precipitation = models.FloatField()
