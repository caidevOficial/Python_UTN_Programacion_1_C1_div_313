
def do_bubble_sort(mi_lista: list, orden: str = 'ASC') -> list:
    cantidad_cambios = 0
    tamanio_lista = len(mi_lista)
    for vueltas in range(tamanio_lista):

        for primer_indice in range(0, tamanio_lista - vueltas - 1):

            siguiente_indice = primer_indice + 1
            
            if mi_lista[primer_indice] > mi_lista[siguiente_indice] and orden == 'ASC' or\
               mi_lista[primer_indice] < mi_lista[siguiente_indice] and orden == 'DES':
                auxiliar = mi_lista[primer_indice]
                mi_lista[primer_indice] = mi_lista[siguiente_indice]
                mi_lista[siguiente_indice] = auxiliar
                cantidad_cambios += 1
    
    print(f'Bubble sort: Cantidad de cambios realizados: {cantidad_cambios}')
    return mi_lista





# ============ Testeamos tiempo y rendimiento ============
import random
from test_sorts import test_sort

cantidad = 10000
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

# 5K elementos tardo 2 seg 401 ms
# 10K elementos tardo 8 seg 942 ms
test_sort(do_bubble_sort, mi_lista_test, 'ASC',sort_name='Bubble Sort')

# lista = [5,4,9,7,1,6,10,0,25,-10,-8,-15,-1]
# lista_ordenada = do_bubble_sort(lista)
# print(lista_ordenada)