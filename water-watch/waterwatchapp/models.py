# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class WaterConsumption(models.Model):
    Id = models.IntegerField(primary_key = True)
    Suburb = models.CharField(max_length = 100)
    NoOfSingleResProp = models.IntegerField()
    AvgMonthlyKL = models.IntegerField()
    AvgMonthlyKLPredicted = models.IntegerField()
    PredictionAccuracy = models.IntegerField()
    Month = models.CharField(max_length = 50)
    Year = models.IntegerField()
    DateTime = models.DateTimeField()
    geom = models.PointField()

    def __str__(self):
        return self.Suburb

    class Meta:
        verbose_name_plural = 'WaterConsumption'

class Coronavirus(models.Model):
    Id = models.IntegerField(primary_key = True)
    Country = models.CharField(max_length = 50)
    Province = models.CharField(max_length = 50)
    CountryProvince = models.CharField(max_length = 100)
    NoOfConfirmed = models.IntegerField()
    NoOfRecovered = models.IntegerField()
    NoOfDeath = models.IntegerField()
    Day = models.IntegerField()
    geom = models.PointField()

    def __str__(self):
        return self.CountryProvince

    class Meta:
        verbose_name_plural = 'Coronavirus'
