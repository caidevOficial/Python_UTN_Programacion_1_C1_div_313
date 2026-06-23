from utn_fra_datasets.datasets import lista_diccionario_heroes_small, lista_diccionario_heroes_hard_small
from funciones import leer_json, escribir_json

ARCHIVO_JSON = './18_archivos/info.json'

info_heroes = {
    "info": lista_diccionario_heroes_small
}

if __name__ == '__main__':
    escribir_json(ARCHIVO_JSON, info_heroes)
    informacion = leer_json(ARCHIVO_JSON)
    
    lista_heroes = informacion.get('info')
    primeros_dos_heroes = lista_heroes[:2]
    
    
    print(primeros_dos_heroes)