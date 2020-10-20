from pyproj import Transformer
import numpy as np 
import pandas as pd 
# Un código simple para convertir de un sistemas de coordenadas geográficas a planas

# Reporte sismos servicio geologico, coordenadas geográficas
sismos = pd.read_excel('reporte763.xlsx')
lats = np.asarray(sismos['LATITUD (grados)'])
lons = np.asarray(sismos['LONGITUD (grados)'])

transformer = Transformer.from_crs(4326, 3116)
puntos = list(zip(lats, lons))


nuevasCoordenadas = []
for pt in transformer.itransform(puntos): 
    nuevasCoordenadas.append(pt)

# mostrar las cuatro primeras coordenadas viejas y nuevas
print("Conversión de coordenadas geográficas a planas\n")
print("Geográficas (4326) \t -> \t  Planas (3116)\n")
for i in range(4):
    print(puntos[i], "\t\t", nuevasCoordenadas[i])