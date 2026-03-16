from pyproj import Transformer
import requests
import pandas as pd

class DatosCalidadAire:
    def __init__(self):
        self.url = "https://datos.comunidad.madrid/api/action/datastore_search?id=c05f6436-783e-4b04-b0d2-47848daea984"
        self.transformer = Transformer.from_crs("EPSG:25830", "EPSG:4326", always_xy=True)
        response = requests.get(self.url)
        data = response.json()
        records = data["result"]["records"]
        self.df = pd.DataFrame(records)
        self.df["lon"], self.df["lat"] = self.transformer.transform(
            self.df["estacion_coord_UTM_ETRS89_x"].values,
            self.df["estacion_coord_UTM_ETRS89_y"].values
        )

    def obtener_datos(self):
        return self.df