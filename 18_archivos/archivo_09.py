from variables import ARCHIVO_HEROES, CODIFICACION, ARCHIVO_ARGENTO
from funciones import split_texto


def parsear_dataset_matriz(datos: list[str]) -> list[list]:
    mi_matriz = []
    for linea in datos:
        if datos.index(linea) == 0:
            continue
        linea = linea.replace('\n', '')
        datos_linea = split_texto(linea, ',')
        mi_matriz.append(datos_linea)
    return mi_matriz

def parsear_dataset_lidict(datos: list[str]) -> list[dict]:
    str_claves_limpias = datos.pop(0).replace('\n', '')
    claves = split_texto(str_claves_limpias, ',')
    lista_dict_heroes = []

    for heroe in datos:
        heroe = heroe.replace('\n', '')
        datos_heroe = split_texto(heroe, ',')
        heroe_dict = {}

        for indice_clave in range(len(claves)):
            heroe_dict.update(
                {claves[indice_clave] : datos_heroe[indice_clave]}
            )
        lista_dict_heroes.append(heroe_dict)
    return lista_dict_heroes



def leer_dataset(ruta: str) ->list[str]:

    
    with open(ruta, 'r', encoding=CODIFICACION) as file:
        contenido = file.readlines()

    return contenido

contenido = leer_dataset(ARCHIVO_ARGENTO)
li_di_heroes = parsear_dataset_lidict(contenido)
# matriz = parsear_dataset_matriz(contenido)
print(li_di_heroes)