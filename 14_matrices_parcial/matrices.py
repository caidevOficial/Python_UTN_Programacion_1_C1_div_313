import op_matematicas as mate

def do_selection_sort_vt(matriz: list[list], indice_col_a_ordenar: int, modo: str = 'DES'):
    for indice_fila in range(len(matriz) - 1):
        indice_elem_menor = indice_fila

        for indice_sig_fila in range(indice_fila + 1, len(matriz)):

            if matriz[indice_elem_menor][indice_col_a_ordenar] < matriz[indice_sig_fila][indice_col_a_ordenar] and modo == 'DES' or\
               matriz[indice_elem_menor][indice_col_a_ordenar] > matriz[indice_sig_fila][indice_col_a_ordenar] and modo == 'ASC':
                indice_elem_menor = indice_sig_fila
            
        if indice_elem_menor != indice_fila:
            aux = matriz[indice_elem_menor]
            matriz[indice_elem_menor] = matriz[indice_fila]
            matriz[indice_fila] = aux

def mostrar_datos_pokemons(matriz: list[list]):

    cant_col = len(matriz[0])
    cant_fil = len(matriz)

    for fila in range(cant_fil):

        info = ''

        for col in range(cant_col):
            info += f'{matriz[fila][col]},'
        
        info = info[0:-1]
        print(info)

def obtener_indices_filas_vt(matriz: list[list], indice_col: int, modo='igual', valor=None) -> list:
    lista_indices_filas = []

    for indice_fila in range(len(matriz)):
        if modo == 'igual' and matriz[indice_fila][indice_col] == valor or\
           modo == 'mayor' and matriz[indice_fila][indice_col] > valor or\
           modo == 'menor' and matriz[indice_fila][indice_col] < valor:
            lista_indices_filas.append(indice_fila)
    return lista_indices_filas

def crear_filtro_por_indices(matriz: list[list], lista_indices: list) -> list[list]:
    matriz_filtrada = []
    for indice_fila in lista_indices:
        matriz_filtrada.append(matriz[indice_fila])
    return matriz_filtrada

def filtrar_pokemons(matriz_poke: list[list], indice_col: int, modo: str = 'mayor', valor = None) -> list[list]:
    matriz_filtrada = []

    # for indice_fila in range(len(matriz_poke)):
    #     if modo == 'igual' and matriz_poke[indice_fila][indice_col] == valor or\
    #        modo == 'mayor' and matriz_poke[indice_fila][indice_col] > valor or\
    #        modo == 'menor' and matriz_poke[indice_fila][indice_col] < valor:
    #         matriz_filtrada.append(matriz_poke[indice_fila])
    
    for fila in matriz_poke:
        if modo == 'igual' and fila[indice_col] == valor or\
           modo == 'mayor' and fila[indice_col] > valor or\
           modo == 'menor' and fila[indice_col] < valor:
            matriz_filtrada.append(fila)
    return matriz_filtrada

def mostrar_pokemones_promedio(matriz_poke: list[list]):
    promedio = mate.obtener_promedio_t(matriz_poke, 3)
    matriz_filtrada = filtrar_pokemons(matriz_poke, 3, modo='mayor', valor=promedio)
    mostrar_datos_pokemons(matriz_filtrada)

def mostrar_pokemones_fuego(matriz_poke: list[list]):
    matriz_filtrada = filtrar_pokemons(matriz_poke, 4, modo='igual', valor='legendario')
    do_selection_sort_vt(matriz_filtrada, 3)
    mostrar_datos_pokemons(matriz_filtrada)

def mostrar_pokemones_fuego(matriz_poke: list[list]):
    matriz_filtrada = filtrar_pokemons(matriz_poke, 2, modo='igual', valor='fuego')
    mostrar_datos_pokemons(matriz_filtrada)

def mostrar_pokemons_fuertes(matriz_poke: list[list]):
    maximo_poder = mate.obtener_mayor_vt(matriz_poke, 3)
    matriz_filtrada = filtrar_pokemons(matriz_poke, 3, modo='igual', valor=maximo_poder)
    
    print(f'El poder maximo es: {maximo_poder} y estos pokémons lo cumplen:')
    mostrar_datos_pokemons(matriz_filtrada)

def mostrar_pokemons_porcentaje(matriz_poke: list[list]):
    por_leg = mate.obtener_porcentaje(matriz_poke, 4, 'legendario')
    por_nor = mate.obtener_porcentaje(matriz_poke, 4, valor='normal')
    cantidad_total = len(matriz_poke)

    """
    [
        ['legendario', 33.3],
        ['normal', 66.6]
    ]
    """

    mensaje =\
    f"""
    Total Pokémons: {cantidad_total}
    Porcentaje Legendario: {por_leg} %
    Porcentaje Normal: {por_nor} %
    """
    print(mensaje)

def trasponer_matriz(matriz: list[list]) -> list[list]:
    matriz_t = []

    cant_col = len(matriz[0])
    cant_fil = len(matriz)

    for indice_col in range(cant_col):

        nueva_fila = []

        for indice_fila in range(cant_fil):
            elemento = matriz[indice_fila][indice_col]
            nueva_fila.append(elemento)

        matriz_t.append(nueva_fila)
    
    return matriz_t