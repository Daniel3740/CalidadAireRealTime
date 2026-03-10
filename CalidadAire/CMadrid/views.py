from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'CMadrid/index.html')

def map_view(request):
    return render(request, 'CMadrid/map.html')

def madrid_view(request):
    return render(request, 'CMadrid/madrid.html')
