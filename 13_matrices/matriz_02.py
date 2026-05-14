
def crear_matriz(filas: int, col: int) -> list[list]:
    matriz = []

    for num_f in range(filas):

        lista_fila = [0] * col
        matriz.append(lista_fila)


    return matriz

from matriz_01 import mostrar_datos_matriz_cf, mostrar_datos_matriz_fc

# filas = int(input('Ingrese la cantidad de filas: '))
# columnas = int(input('Ingrese la cantidad de columnas: '))

# matriz = crear_matriz(filas, columnas)


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


matriz_pokemons_t = [
    [244,'entei','fuego',30,'legendario'],
    [28,'sandslash','suelo',15,'normal'],
    [584,'vanilluxe','hielo',15,'normal'],
    [26,'raichu','eléctrico',20,'normal'],
    [9,'blastoise','agua',18,'normal']
]

mostrar_datos_matriz_cf(matriz_pokemons_t)
print('')
mostrar_datos_matriz_fc(matriz_pokemons_t)

# print(matriz_pokemons)