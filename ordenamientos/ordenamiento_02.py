
def do_selection_sort(mi_lista: list, orden: str = 'ASC') -> list:
    cantidad_cambios = 0
    tamanio_lista = len(mi_lista)

    for primer_indice in range(tamanio_lista - 1):

        indice_mas_chico = primer_indice

        for siguiente_indice in range(primer_indice + 1, tamanio_lista):

            if mi_lista[indice_mas_chico] > mi_lista[siguiente_indice] and orden == 'ASC' or\
               mi_lista[indice_mas_chico] < mi_lista[siguiente_indice] and orden == 'DES':
                indice_mas_chico = siguiente_indice
        
        if indice_mas_chico != primer_indice:
            auxiliar = mi_lista[indice_mas_chico]
            mi_lista[indice_mas_chico] = mi_lista[primer_indice]
            mi_lista[primer_indice] = auxiliar
            cantidad_cambios += 1

    print(f'Selection Sort: Cantidad de cambios realizados: {cantidad_cambios}')
    return mi_lista

# ============ Testeamos tiempo y rendimiento ============
import random
from test_sorts import test_sort

cantidad = 1000
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

# 5K elementos 1 seg 149 ms
# 10K elementos 3 seg 590 ms
test_sort(do_selection_sort, mi_lista_test, 'DES', sort_name='Selection Sort')