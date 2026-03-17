import pandas as pd

from .datosMadrid import df_final, generar_interpolaciones

class DatosCalidadAire:
    def __init__(self):
        # Cargamos el DataFrame procesado por datosMadrid
        self.df = df_final.copy()

        # Guardamos los datos de interpolación antes de renombrar columnas
        self.interpolaciones = generar_interpolaciones(self.df)

        # Convertir NaN a None para evitar 'nan' inválido en JS al renderizar datos en template
        self.df = self.df.astype(object).where(pd.notnull(self.df), None)

        # Renombrar las columnas que llegaron como LATITUD/LONGITUD a latitud/longitud
        # y mantener compatibilidad con el uso anterior de lat/lon en las plantillas
        if "LATITUD" in self.df.columns and "LONGITUD" in self.df.columns:
            self.df = self.df.rename(columns={"LATITUD": "latitud", "LONGITUD": "longitud"})
            self.df["lat"] = self.df["latitud"]
            self.df["lon"] = self.df["longitud"]

        # Compatibilidad con las claves de estación usadas en templates / JS
        # (por si se esperan como `estacion_codigo`, `estacion_municipio`, `estacion_direccion_postal` etc.)
        if "COD_ESTACION" in self.df.columns:
            self.df = self.df.rename(columns={"COD_ESTACION": "estacion_codigo"})
        if "NOMBRE_ESTACION" in self.df.columns:
            self.df = self.df.rename(columns={"NOMBRE_ESTACION": "estacion_municipio"})
        if "NOM_TIPO" in self.df.columns and "estacion_direccion_postal" not in self.df.columns:
            self.df["estacion_direccion_postal"] = self.df["NOM_TIPO"]

    def obtener_datos(self):
        return self.df

    def obtener_interpolaciones(self):
        return self.interpolaciones
