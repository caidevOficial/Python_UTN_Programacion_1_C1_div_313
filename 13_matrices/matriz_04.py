
def do_selection_sort(matriz: list[list], indice_fila_a_ordenar: int, modo: str= 'DES'):

    for indice_col in range(len(matriz[indice_fila_a_ordenar]) - 1):

        indice_elem_menor = indice_col

        for indice_sig_col in range(indice_col + 1, len(matriz[indice_fila_a_ordenar])):

            if matriz[indice_fila_a_ordenar][indice_elem_menor] < matriz[indice_fila_a_ordenar][indice_sig_col] and modo == 'DES' or\
               matriz[indice_fila_a_ordenar][indice_elem_menor] > matriz[indice_fila_a_ordenar][indice_sig_col] and modo == 'ASC':
                indice_elem_menor = indice_sig_col
        
        if indice_elem_menor != indice_col:

            for indice_fila in range(len(matriz)):

                # Forma Pythonesca
                # matriz[indice_fila][indice_elem_menor], matriz[indice_fila][indice_col] =\
                # matriz[indice_fila][indice_col], matriz[indice_fila][indice_elem_menor]

                # Forma clásica
                aux = matriz[indice_fila][indice_col]
                matriz[indice_fila][indice_col] = matriz[indice_fila][indice_elem_menor]
                matriz[indice_fila][indice_elem_menor] = aux

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
                

from matriz_02 import matriz_pokemons
from matriz_03 import mostrar_datos_matriz_cf, mostrar_datos_matriz_fc, trasponer_matriz


if __name__ == '__main__':
    print("Antes de ordenar")
    matriz_t = trasponer_matriz(matriz_pokemons)
    mostrar_datos_matriz_fc(matriz_t)
    do_selection_sort_vt(matriz_t, 0)
    print("\nDespues de ordenar\n")
    mostrar_datos_matriz_fc(matriz_t)