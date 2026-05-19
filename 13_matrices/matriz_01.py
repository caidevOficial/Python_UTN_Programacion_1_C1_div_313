
matriz_persona = [
    ["Pepe", "Moni"],
    [54, 45],
    ["M", "F"]
]

lista_nombres = ["Pepe", "Moni"]
lista_edades = [54, 45]
lista_generos = ["M", "F"]

nueva_matriz_personas = [
    lista_nombres,
    lista_edades,
    lista_generos
]

# print(nueva_matriz_personas)

def mostrar_datos_matriz_cf(matriz: list[list]):

    cant_col = len(matriz[0])
    cant_fil = len(matriz)

    for col in range(cant_col):

        info = ''
        for fil in range(cant_fil):
            info += f'{matriz[fil][col]},'

        info = info[0:-1]        
        print(info)

def mostrar_datos_matriz_fc(matriz: list[list]):

    cant_col = len(matriz[0])
    cant_fil = len(matriz)

    for fila in range(cant_fil):

        info = ''

        for col in range(cant_col):
            info += f'{matriz[fila][col]},'
        
        info = info[0:-1]
        print(info)









from utn_fra_datasets.datasets import (
    lista_poke_ids, lista_poke_nombres,
    lista_poke_tipos, lista_poke_poderes,
    lista_poke_condiciones
)

matriz_pokemons = [
    lista_poke_ids, 
    lista_poke_nombres,
    lista_poke_tipos, 
    lista_poke_poderes,
    lista_poke_condiciones
]

if __name__ == '__main__':
    mostrar_datos_matriz_cf(matriz_pokemons)