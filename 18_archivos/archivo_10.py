from variables import ARCHIVO_LOGS, CODIFICACION, ARCHIVO_AUTOS
from utn_fra_datasets.datasets import matriz_concesionaria
from funciones import trasponer_matriz
from archivo_07 import guardar_matriz_archivo
import datetime

from datetime import datetime

def guardar_logs(mensaje: str):

    with open(ARCHIVO_LOGS, 'a', encoding=CODIFICACION) as logs:
        logs.write(f'{mensaje}\n')
        print('[SYSTEM]: NUEVO LOG GUARDADO CON EXITO!')

def generar_fecha_actual_str():
    fecha = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
    return fecha

matriz_t = trasponer_matriz(matriz_concesionaria)

fecha = generar_fecha_actual_str()
guardar_logs(f'{fecha} - Se cargo la matriz de autos')
cabecera_archivo = ['marca', 'modelo', 'cantidad', 'precio_unitario', 'total']
guardar_matriz_archivo(matriz_t, cabecera_archivo, ARCHIVO_AUTOS)


fecha = generar_fecha_actual_str()
guardar_logs(f'{fecha} - Se guardo la matriz de autos en: {ARCHIVO_AUTOS}')