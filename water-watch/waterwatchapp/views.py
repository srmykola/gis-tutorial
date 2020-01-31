from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize
from waterwatchapp.models import WaterConsumption, Coronavirus
from django.template.context import Context
import pandas as pd

# Create your views here.
def waterconsumption_dataset(request):
    waterconsumption = serialize('geojson', WaterConsumption.objects.all())
    return HttpResponse(waterconsumption, content_type = 'json')

def top10_consumers(request):
    #data = WaterConsumption.objects.only('Suburb').order_by('-AvgMonthlyKL')[:20]
    df_top10 = pd.DataFrame.from_records(Coronavirus.objects.all().values())
    #df_top10_x_y = df_top10[['Suburb']]
    df_top10_x_y_sorted = df_top10.sort_values(['NoOfConfirmed'], ascending=False)
    df_top10_x_y = df_top10_x_y_sorted[['CountryProvince', 'NoOfConfirmed']]
    df_top10_rows = df_top10_x_y.head(10)
    df_top10_rows_json = df_top10_rows.to_json(orient='records')
    return HttpResponse(df_top10_rows_json, content_type='json')

def coronavirus_dataset(request):
    coronavirus_response = serialize('geojson', Coronavirus.objects.all())
    return HttpResponse(coronavirus_response, content_type = 'json')

def home(request):
    """ Renders home page """
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
        }
    )
