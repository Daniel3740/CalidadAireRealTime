# CalidadAireRealTime 🌍💨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Leaflet](https://img.shields.io/badge/Leaflet-1.9.4-blue)](https://leafletjs.com/) 
[![Open Data](https://img.shields.io/badge/Open-Data-green)](https://datos.gob.es/es/catalogo/tema/medio-ambiente) 
[![Mapa en Vivo](https://img.shields.io/badge/Mapa-en_vivo-red)](#)

**Visualiza la calidad del aire en tiempo real** usando datos abiertos de estaciones ambientales públicas.  
Representa contaminantes como **PM2.5, PM10, NOx, NO2, O3, SO2 y CO** en un mapa interactivo con heatmaps dinámicos y marcadores personalizados.

---


## 🚀 Características

- Mapas interactivos con [Leaflet](https://leafletjs.com/)  
- Heatmaps dinámicos de todos los contaminantes con [Leaflet.heat](https://github.com/Leaflet/Leaflet.heat)  
- Marcadores personalizados para estaciones de monitoreo  
- Normalización y combinación de datos de múltiples contaminantes  
- Funcionalidad de clic para añadir marcadores temporales y ver información  

---

## 💻 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Daniel3740/CalidadAireRealTime.git
cd CalidadAireRealTime
```
Instala un servidor local (opciones según tu entorno):

Crea un entorno virtual e instala dependencias:
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
pip install -r requirements.txt
```
Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

Abre el navegador y accede a:
```bash
http://127.0.0.1:8000
```
