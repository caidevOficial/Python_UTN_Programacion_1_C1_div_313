from utn_fra_datasets.datasets import matriz_concesionaria
from funciones import trasponer_matriz, join_lista_a_texto

from variables import ARCHIVO_AUTOS, CODIFICACION


def guardar_matriz_archivo(matriz_t: list[list], cabecera: list[str],ruta: str):
    with open(ruta, 'w', encoding=CODIFICACION) as archivo:

        lista_texto = []

        headr = join_lista_a_texto(cabecera, ',') + '\n'
        lista_texto.append(headr)

        for fila in matriz_t:
            texto = join_lista_a_texto(fila, ',') + '\n'
            lista_texto.append(texto)

        archivo.writelines(lista_texto)

cabecera_archivo = ['marca', 'modelo', 'cantidad', 'precio_unitario', 'total']
matriz_t = trasponer_matriz(matriz_concesionaria)
guardar_matriz_archivo(matriz_t, cabecera=cabecera_archivo, ruta=ARCHIVO_AUTOS)