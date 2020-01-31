from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from waterwatchapp.models import WaterConsumption
from waterwatchapp.models import Coronavirus

# Register your models here.

class WaterConsumptionAdmin(LeafletGeoAdmin):
    pass

admin.site.register(WaterConsumption, WaterConsumptionAdmin)

df_excelReader = pd.read_excel('/usr/Desktop/GIS-tutorial/water-watch/waterwatchapp/waterwatch_clean2.xlsx', sheet_name='Sheet1')

for index, row in df_excelReader.iterrows():
    Id = index
    Suburb = row['Suburb']
    NoOfSingleResProp = row['Number of single-residential properties_number']
    AvgMonthlyKL = row['Oct 2017\nkl/month']
    AvgMonthlyKLPredicted = 0
    PredictionAccuracy = 0
    Month = row['Month']
    Year = row['Year']
    DateTime = datetime.now()
    Longitude = row['Longitude']
    Latitude = row['Latitude']

    WaterConsumption(Id = Id, Suburb = Suburb, NoOfSingleResProp = NoOfSingleResProp,
                    AvgMonthlyKL = AvgMonthlyKL, AvgMonthlyKLPredicted = AvgMonthlyKLPredicted,
                    PredictionAccuracy = PredictionAccuracy, Month = Month,
                    Year = Year, DateTime = DateTime, geom = Point(Longitude, Latitude)).save()


class CoronavirusAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Coronavirus, CoronavirusAdmin)

df_excelReader = pd.read_excel('/usr/Desktop/GIS-tutorial/water-watch/waterwatchapp/coronavirus.xlsx', sheet_name='Sheet1')

for index, row in df_excelReader.iterrows():
    Id = index
    Country = row['Country/Region']
    Province = row['Province/State']
    CountryProvince = row['Country/Region'] + ' - ' + row['Province/State']
    NoOfConfirmed = row['Confirmed']
    NoOfRecovered = row['Recovered']
    NoOfDeath = row['Death']
    Longitude = row['longitude']
    Latitude = row['latitude']
    Day = row['day']

    Coronavirus(Id = Id,
        Country = Country,
        Province = Province,
        CountryProvince = CountryProvince,
        NoOfConfirmed = NoOfConfirmed,
        NoOfRecovered = NoOfRecovered,
        NoOfDeath = NoOfDeath,
        Day = Day,
        geom = Point(Longitude, Latitude)).save()
