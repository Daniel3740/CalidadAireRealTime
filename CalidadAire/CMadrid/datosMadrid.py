import requests
import pandas as pd
from datetime import datetime

BASE_URL = "https://ciudadesabiertas.madrid.es/dynamicAPI/API/query"

# -------------------------
# 1. Descargar estaciones
# -------------------------
url_estaciones = f"{BASE_URL}/calair_estaciones.json"
res = requests.get(url_estaciones)
res.raise_for_status()
data_estaciones = res.json()
df_estaciones = pd.DataFrame(data_estaciones["records"])

df_estaciones = df_estaciones[[
    "CODIGO_CORTO", "ESTACION", "DIRECCION",
    "LATITUD", "LONGITUD", "NOM_TIPO"
]]

# -------------------------
# 2. Descargar todas las páginas de mediciones
# -------------------------
def get_all_pages():
    page = 1
    all_data = []

    while True:
        url = f"{BASE_URL}/calair_tiemporeal_ult.json?pageSize=100&page={page}"
        res = requests.get(url)
        res.raise_for_status()

        data = res.json()
        records = data.get("records") or data.get("content") or []
        if not isinstance(records, list):
            records = []

        all_data.extend(records)

        print(f"Página {page} descargada ({len(records)} registros)")

        if "next" not in data or not data.get("next"):
            break

        page += 1

    return pd.DataFrame(all_data)

df_mediciones = get_all_pages()

# -------------------------
# 3. Filtrar solo registros del día actual
# -------------------------
hoy = datetime.now()
ano = str(hoy.year)
mes = str(hoy.month).zfill(2)
dia = str(hoy.day).zfill(2)

df_mediciones = df_mediciones[
    (df_mediciones["ANO"] == ano) &
    (df_mediciones["MES"] == mes) &
    (df_mediciones["DIA"] == dia)
]

# -------------------------
# 4. Contaminantes
# -------------------------
magnitudes = {
    "1": "SO2",
    "6": "CO",
    "8": "NO2",
    "9": "PM2.5",
    "10": "PM10",
    "12": "NOx",
    "14": "O3"
}
df_mediciones["CONTAMINANTE"] = df_mediciones["MAGNITUD"].map(magnitudes)

# -------------------------
# 5. Obtener la última hora disponible
# -------------------------
def ultima_hora(row):
    horas = [f"H{i:02}" for i in range(1, 25)]
    for h in reversed(horas):
        if row.get(h) not in [None, "", "V"]:
            return float(row[h])
    return None

df_mediciones["ULTIMA_HORA"] = df_mediciones.apply(ultima_hora, axis=1)

# -------------------------
# 6. Merge con estaciones
# -------------------------
df_final = df_mediciones.merge(
    df_estaciones,
    left_on="ESTACION",
    right_on="CODIGO_CORTO",
    how="left"
)

df_final = df_final.rename(columns={
    "ESTACION_x": "COD_ESTACION",
    "ESTACION_y": "NOMBRE_ESTACION"
})

df_final = df_final[[
    "COD_ESTACION", "NOMBRE_ESTACION", "CONTAMINANTE",
    "ANO", "MES", "DIA",
    "ULTIMA_HORA",
    "LATITUD", "LONGITUD", "NOM_TIPO"
]]

# Reemplazar NaN por None antes de pasar los datos al render
# (evita `nan` en JavaScript cuando se serializa la lista de estaciones)
df_final = df_final.astype(object).where(pd.notnull(df_final), 'None')

# -------------------------
# 7. Mostrar resultado
# -------------------------
print(df_final.head())