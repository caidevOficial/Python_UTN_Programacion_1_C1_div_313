
def buscar_indice_de_intercambio(indice_inicial: int, tamanio_lista: int, lista_a_comparar: list, orden: str):
    indice_mas_chico = indice_inicial

    for siguiente_indice in range(indice_inicial + 1, tamanio_lista):

        if lista_a_comparar[siguiente_indice] < lista_a_comparar[indice_mas_chico] and orden == 'ASC' or\
            lista_a_comparar[siguiente_indice] > lista_a_comparar[indice_mas_chico] and orden == 'DES':
            indice_mas_chico = siguiente_indice
    
    return indice_mas_chico

def intercambiar_elementos_listas(lista_origen: list, indice_origen: int, indice_destino: int):
    aux = lista_origen[indice_origen]
    lista_origen[indice_origen] = lista_origen[indice_destino]
    lista_origen[indice_destino] = aux

def do_selection_sort(lista_a_comparar: list, lista_b: list, lista_c: list, lista_d: list, orden: str = 'ASC') -> list:

    tamanio_lista = len(lista_a_comparar)

    for indice_inicial in range(tamanio_lista - 1):

        indice_mas_chico = buscar_indice_de_intercambio(indice_inicial, tamanio_lista, lista_a_comparar, orden)

        if indice_mas_chico != indice_inicial:

            intercambiar_elementos_listas(lista_a_comparar, indice_mas_chico, indice_inicial)
            intercambiar_elementos_listas(lista_b, indice_mas_chico, indice_inicial)
            intercambiar_elementos_listas(lista_c, indice_mas_chico, indice_inicial)
            intercambiar_elementos_listas(lista_d, indice_mas_chico, indice_inicial)

    return None


def mostrar_datos(lista_marca: list, lista_modelo: list, lista_precio: list, lista_cantidad: list):
    for indice in range(len(lista_marca)):

        marca = lista_marca[indice]
        modelo = lista_modelo[indice]
        precio = lista_precio[indice]
        cantidad = lista_cantidad[indice]

        dato = f'{marca},{modelo},{precio},{cantidad}'
        print(dato)

from utn_fra_datasets.datasets import (
    lista_autos_precios, lista_autos_marcas, 
    lista_autos_modelos, lista_autos_cantidades
)





mostrar_datos(lista_autos_marcas, lista_autos_modelos, lista_autos_precios, lista_autos_cantidades)
print()
do_selection_sort(lista_autos_modelos, lista_autos_cantidades, lista_autos_marcas, lista_autos_precios, orden='ASC')
mostrar_datos(lista_autos_marcas, lista_autos_modelos, lista_autos_precios, lista_autos_cantidades)
print()
do_selection_sort(lista_autos_modelos, lista_autos_cantidades, lista_autos_marcas, lista_autos_precios, orden='DES')
mostrar_datos(lista_autos_marcas, lista_autos_modelos, lista_autos_precios, lista_autos_cantidades)
