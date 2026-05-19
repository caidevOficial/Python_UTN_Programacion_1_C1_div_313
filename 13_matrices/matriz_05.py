

# Filtrar y mostrar pokemons legendarios
# Version T

"""
[
    [ID,ID,ID],
    [NOMBRE, NOMBRE, NOMBRE],
    [TIPO,TIPO,TIPO],
    [PODER,PODER,PODER]
]
"""

def crear_matriz_vacia(cantidad_filas: int):
    matriz = []
    for nro_fila in range(cantidad_filas):
        matriz.append([])
    return matriz

def filtrar_por_condicion(matriz: list[list], indice_fila_buscar: int, valor: str = ''):
    matriz_filtrada = crear_matriz_vacia(len(matriz))

    cant_col = len(matriz[indice_fila_buscar])

    for indice_col in range(cant_col):

        if matriz[indice_fila_buscar][indice_col] == valor:

            for indice_fila in range(len(matriz)):
                matriz_filtrada[indice_fila].append(matriz[indice_fila][indice_col])
    return matriz_filtrada



"""
[
    [ID, NOMBRE, TIPO, PODER, CONDICION],
    [ID, NOMBRE, TIPO, PODER, CONDICION]
]
"""
def filtrar_por_condicion_vt(matriz: list[list], indice_col_buscar: int, valor: str = ''):
    matriz_filtrada = []

    # for indice_fila in range(len(matriz)):
    #     if matriz[indice_fila][indice_col_buscar] == valor:
    #         matriz_filtrada.append(matriz[indice_fila])
    
    for fila in matriz:
        if fila[indice_col_buscar] == valor:
            matriz_filtrada.append(fila)

    return matriz_filtrada

if __name__ == '__main__':
    from matriz_01 import matriz_pokemons, mostrar_datos_matriz_fc, mostrar_datos_matriz_cf
    from matriz_03 import trasponer_matriz
    from matriz_04 import do_selection_sort_vt, do_selection_sort

    # # version T
    # matriz_poke_t = trasponer_matriz(matriz_pokemons)
    # do_selection_sort_vt(matriz_poke_t, 3)

    # # filtrar
    # matriz_t_filtrada = filtrar_por_condicion_vt(matriz_poke_t, 4, 'legendario')

    # mostrar_datos_matriz_fc(matriz_t_filtrada)

    do_selection_sort(matriz_pokemons, 3)
    matriz_filtrada = filtrar_por_condicion(matriz_pokemons, 4, valor='legendario')
    mostrar_datos_matriz_cf(matriz_filtrada)
