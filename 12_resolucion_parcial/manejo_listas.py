import op_matematicas as mate

def mostrar_info_completa_pokemon(indice: int, ids: list, nombres: list, tipos: list, poderes: list, condiciones: list):
    poke_id = ids[indice]
    poke_nombre = nombres[indice]
    poke_tipo = tipos[indice]
    poke_poder = poderes[indice]
    poke_condi = condiciones[indice]

    info = f'{poke_id},{poke_nombre},{poke_tipo},{poke_poder},{poke_condi}'
    print(info)

def mostrar_info_completa_pokemones(ids: list, nombres: list, tipos: list, poderes: list, condiciones: list):
    for indice in range(len(nombres)):

        mostrar_info_completa_pokemon(indice, ids, nombres,
                                       tipos, poderes,
                                       condiciones)

def obtener_indices(lista: list, modo='igual', valor=None) -> list:
    lista_resultado = []

    for indice_elm in range(len(lista)):
        if modo == 'igual' and lista[indice_elm] == valor or\
           modo == 'mayor' and lista[indice_elm] > valor or\
           modo == 'menor' and lista[indice_elm] < valor:
            lista_resultado.append(indice_elm)
    return lista_resultado

def mostrar_pokemones_promedio(ids: list, nombres: list, tipos: list, poderes: list, condiciones: list):
    promedio = mate.obtener_promedio(poderes)
    indices_coincidencias = obtener_indices(poderes, modo='mayor', valor=promedio)

    print(f'El promedio de poder es: {promedio} y es superado por los siguientes pokémons')
    for indice in indices_coincidencias:
        mostrar_info_completa_pokemon(indice, ids, nombres, 
                                       tipos, poderes,
                                       condiciones)

def do_selection_sort(lista_principal: list, lista_2: list, lista_3: list, lista_4: list, lista_5: list, modo='ASC'):

    for indice_a in range(len(lista_principal) - 1):
        
        # esto sería una funcion
        indice_menor = indice_a
        for indice_b in range(indice_a + 1, len(lista_principal)):

            if lista_principal[indice_menor] > lista_principal[indice_b] and modo == 'ASC' or\
               lista_principal[indice_menor] < lista_principal[indice_b] and modo == 'DES':
                indice_menor = indice_b
        # hasta aca

        # Esto seria otra funcion
        if indice_menor != indice_a:
            lista_principal[indice_menor], lista_principal[indice_a] =\
            lista_principal[indice_a], lista_principal[indice_menor]

            lista_2[indice_menor], lista_2[indice_a] =\
            lista_2[indice_a], lista_2[indice_menor]

            lista_3[indice_menor], lista_3[indice_a] =\
            lista_3[indice_a], lista_3[indice_menor]

            lista_4[indice_menor], lista_4[indice_a] =\
            lista_4[indice_a], lista_4[indice_menor]

            lista_5[indice_menor], lista_5[indice_a] =\
            lista_5[indice_a], lista_5[indice_menor]
        # hasta acá


def mostrar_pokemones_legendarios(ids: list, nombres: list, tipos: list, poderes: list, condiciones: list):
    
    do_selection_sort(poderes, nombres, ids, condiciones, tipos, modo='DES')
    indices_coincidencias = obtener_indices(condiciones, modo='igual', valor='legendario')

    print(f'Pokémons Legendarios ordenados segun Poder DES')
    for indice in indices_coincidencias:
        mostrar_info_completa_pokemon(indice, ids, nombres, 
                                       tipos, poderes,
                                       condiciones)

def mostrar_pokemones_fuego(ids: list, nombres: list, tipos: list, poderes: list, condiciones: list):
    do_selection_sort(ids, nombres, poderes, condiciones, tipos, modo='ASC')
    indices_coincidencias = obtener_indices(tipos, modo='igual', valor='fuego')

    print(f'Pokémons Tipo Fuego ordenados segun ID ASC')
    for indice in indices_coincidencias:
        mostrar_info_completa_pokemon(indice, ids, nombres, 
                                       tipos, poderes,
                                       condiciones)

def mostrar_pokemon_mas_fuerte_v1(ids: list, nombres: list, tipos: list, poderes: list, condiciones: list):
    
    do_selection_sort(poderes, ids, nombres, condiciones, tipos, modo='DES')

    print(f'VERSION 1: El pokémon mas fuerte es el siguiente:')
    mostrar_info_completa_pokemon(0, ids, nombres, tipos, poderes, condiciones)

def mostrar_pokemon_mas_fuerte_v2(ids: list, nombres: list, tipos: list, poderes: list, condiciones: list):
    mayor_poder = mate.obtener_mayor(poderes)
    indice_coincidencias = obtener_indices(poderes, modo='igual', valor=mayor_poder)

    print(f'VERSION 2: El pokémon mas fuerte es/son el siguiente:')
    for indice in indice_coincidencias:
        mostrar_info_completa_pokemon(indice, ids, nombres,
                                      tipos, poderes, condiciones)

def mostrar_porcentajes_condiciones(condiciones: list):
    porcentaje_legen = mate.obtener_porcentaje(condiciones, 'legendario')
    porcentaje_normal = mate.obtener_porcentaje(condiciones, 'normal')
    # porcentaje_normal = 100 - porcentaje_legen

    mensaje =\
    f"""
    Porcentajes:
    Legendarios: {porcentaje_legen} %
    Normales: {porcentaje_normal} %
    """
    print(mensaje)