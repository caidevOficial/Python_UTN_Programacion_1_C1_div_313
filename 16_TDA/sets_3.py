set_1 = {2,5,6,3,7,4,8}

set_2 = {2,5,6,3,7,4}

# print(
#     set_1.issubset(set_2),
#     set_2.issuperset(set_1),
    
# )

def is_sub_list(source: list, destiny: list) -> bool:
    # source <= destiny
    # todo source -> destiny
    tamanio_correcto = len(source) <= len(destiny)

    if not tamanio_correcto:
        es_sub_lista = False
    else:
        es_sub_lista = True
        for elemento in source:
            if elemento not in destiny:
                es_sub_lista = False
                break

    return es_sub_lista

if __name__ == '__main__':
    lista_1 = [1,2,3]
    lista_2 = [1,4,5,2,3,6]

    print(is_sub_list(lista_1, lista_2))
