
def do_quick_sort(mi_lista: list, orden: str = 'ASC') -> list:
    if len(mi_lista) < 2:
        return mi_lista
    
    pivot = mi_lista.pop()

    lista_pivot = [pivot]
    lista_grandes = []
    lista_chiquitos = []

    for elemento in mi_lista:
        if elemento > pivot:
            lista_grandes.append(elemento)
        else:
            lista_chiquitos.append(elemento)
    if orden == 'ASC':
        return do_quick_sort(lista_chiquitos, orden) + lista_pivot + do_quick_sort(lista_grandes, orden)
    else:
        return do_quick_sort(lista_grandes, orden) + lista_pivot + do_quick_sort(lista_chiquitos, orden)



# ============ Testeamos tiempo y rendimiento ============
import random
from test_sorts import test_sort

cantidad = 5
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

print(do_quick_sort(mi_lista_test, 'ASC'))


# test_sort(do_quick_sort, mi_lista_test, 'DES', sort_name='Quick Sort')