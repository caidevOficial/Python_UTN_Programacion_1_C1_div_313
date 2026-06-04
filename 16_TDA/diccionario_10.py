from utn_fra_datasets.datasets import lista_dict_pokemones, lista_diccionario_heroes_small
from diccionario_09 import do_selection_sort


do_selection_sort(lista_diccionario_heroes_small, ordenar_por='fuerza', modo='DES')
# for heroe in lista_diccionario_heroes_small:
#     print(heroe)
    # print(f'{heroe.get('nombre')} - {heroe.get('fuerza')}')

# color_ojos = 'Blue'
# alineacion = 'good'


def filtrar_elementos(elementos: list[dict], filtrar_por: str, valor_buscado: str) -> list[dict]:

    filtrados = []

    for elemento in elementos:
        if elemento.get(filtrar_por) == valor_buscado:
            filtrados.append(elemento)
    
    return filtrados



filtrado_1 = filtrar_elementos(lista_diccionario_heroes_small, filtrar_por='color_ojos', valor_buscado='Blue')
filtrado_1 = filtrar_elementos(filtrado_1, filtrar_por='alineacion', valor_buscado='good')

# for heroe in filtrado_1:
#     # print(heroe)
#     print(f'{heroe.get('nombre')} - {heroe.get('color_ojos')} - {heroe.get('alineacion')}')

