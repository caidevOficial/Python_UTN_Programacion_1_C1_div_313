from utn_fra_datasets.datasets import lista_diccionario_heroes_small, lista_diccionario_heroes
from funciones import trasponer_matriz, join_lista_a_texto

from variables import ARCHIVO_HEROES, CODIFICACION

def extraer_datos_dict(target: list[str], diccionario: dict, separador: str, tipo_dato: str):
    
    if tipo_dato == 'keys':
        datos = list(diccionario.keys())
    else:
        datos = list(diccionario.values())
    headr = join_lista_a_texto(datos, separador) + '\n'
    target.append(headr)

def crear_texto_datos(dataset: list[dict]):
    lista_texto = []
    extraer_datos_dict(lista_texto, dataset[0], ',', 'keys')
    for heroe in dataset:
        extraer_datos_dict(lista_texto, heroe, ',', 'values')
    return lista_texto

def guardar_dataset_dict_archivo(dataset: list[dict], ruta: str):

    with open(ruta, 'w', encoding=CODIFICACION) as file:
        lista_texto = crear_texto_datos(dataset)
        file.writelines(lista_texto)

guardar_dataset_dict_archivo(lista_diccionario_heroes, ARCHIVO_HEROES)
