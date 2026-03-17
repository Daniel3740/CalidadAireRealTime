from django.shortcuts import render
from .apiMadrid import DatosCalidadAire
import json
import pandas as pd

# Create your views here.

def index(request):
    return render(request, 'CMadrid/index.html')

def map_view(request):
    data_loader = DatosCalidadAire()
    df = data_loader.obtener_datos()
    interpolaciones_data = data_loader.obtener_interpolaciones()

    # Convertir NaN a null en JSON para evitar token JS no válido (nan en minúsculas)
    stations_data = df.astype(object).where(pd.notnull(df), None).to_dict('records')
    stations = json.dumps(stations_data, ensure_ascii=False)
    interpolaciones = json.dumps(interpolaciones_data, ensure_ascii=False)

    context = {
        'stations': stations,
        'interpolaciones': interpolaciones,
    }
    return render(request, 'CMadrid/map.html', context)

def madrid_view(request):
    data_loader = DatosCalidadAire()
    df = data_loader.obtener_datos()
    stations = df.to_dict('records')
    context = {'stations': stations}
    return render(request, 'CMadrid/madrid.html', context)
