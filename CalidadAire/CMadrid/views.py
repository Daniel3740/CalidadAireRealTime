from django.shortcuts import render
from .apiMadrid import DatosCalidadAire
import json

# Create your views here.

def index(request):
    return render(request, 'CMadrid/index.html')

def map_view(request):
    data_loader = DatosCalidadAire()
    df = data_loader.obtener_datos()
    stations = df.to_dict('records')
    context = {'stations': json.dumps(stations)}
    return render(request, 'CMadrid/map.html', context)

def madrid_view(request):
    return render(request, 'CMadrid/madrid.html')
