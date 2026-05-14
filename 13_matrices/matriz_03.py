
from utn_fra_datasets.datasets import (
    lista_poke_ids, lista_poke_nombres,
    lista_poke_tipos, lista_poke_poderes,
    lista_poke_condiciones
)

matriz_pokemons = [
    lista_poke_ids[0:5], 
    lista_poke_nombres[0:5],
    lista_poke_tipos[0:5], 
    lista_poke_poderes[0:5],
    lista_poke_condiciones[0:5]
]


# matriz_pokemons_t = [
#     [244,'entei','fuego',30,'legendario'],
#     [28,'sandslash','suelo',15,'normal'],
#     [584,'vanilluxe','hielo',15,'normal'],
#     [26,'raichu','eléctrico',20,'normal'],
#     [9,'blastoise','agua',18,'normal']
# ]

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


from matriz_01 import mostrar_datos_matriz_cf, mostrar_datos_matriz_fc


mostrar_datos_matriz_cf(matriz_pokemons)
print('')
matriz_t = trasponer_matriz(matriz_pokemons)

mostrar_datos_matriz_fc(matriz_t)