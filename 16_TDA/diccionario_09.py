from utn_fra_datasets.datasets import lista_dict_pokemones, lista_diccionario_heroes_small

def do_selection_sort(elementos: list[dict], ordenar_por: str, modo : str = 'ASC'):

    tamanio_lista = len(elementos)

    for indice_a in range(tamanio_lista - 1):

        indice_menor = indice_a

        for indice_b in range(indice_a + 1, tamanio_lista):
            
            diccionario_im = elementos[indice_menor]
            diccionario_ib = elementos[indice_b]

            if diccionario_im.get(ordenar_por) > diccionario_ib.get(ordenar_por) and modo == 'ASC' or\
               diccionario_im.get(ordenar_por) < diccionario_ib.get(ordenar_por) and modo == 'DES':
                indice_menor = indice_b
        
        if indice_menor != indice_a:
            elementos[indice_menor], elementos[indice_a] =\
            elementos[indice_a], elementos[indice_menor]

def do_quick_sort(elementos: list[dict], ordenar_por: str, modo : str = 'ASC') -> list[dict]:
    if len(elementos) < 2:
        return elementos
    
    pivot = elementos.pop()
    mas_grandes = []
    mas_chicos = []

    for elemento in elementos:
        if elemento.get(ordenar_por) > pivot.get(ordenar_por):
            mas_grandes.append(elemento)
        else:
            mas_chicos.append(elemento)
    
    if modo == 'ASC':
        primer_lista = mas_chicos
        segunda_lista = mas_grandes
    else:
        primer_lista = mas_grandes
        segunda_lista = mas_chicos
    
    return do_quick_sort(primer_lista, ordenar_por, modo) +\
           [pivot] +\
           do_quick_sort(segunda_lista, ordenar_por, modo)

lista_ordenada = do_quick_sort(lista_dict_pokemones, ordenar_por='poder',modo='ASC')

# for pokemon in lista_ordenada:
#     print(pokemon)