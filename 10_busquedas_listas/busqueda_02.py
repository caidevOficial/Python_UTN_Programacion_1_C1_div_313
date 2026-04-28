

"""
1 - Obtener el/los indices de un tipo específico de pokémon
"""

def buscar_indices_tipo_poke(lista_poke: list, tipo: str) -> list:
    indices_tipos_elegidos = []

    for indice_actual in range(len(lista_poke)):
        if lista_poke[indice_actual] == tipo:
            indices_tipos_elegidos.append(indice_actual)

    return indices_tipos_elegidos

if __name__ == '__main__':
    condicion = [
        "normal", "fuego", "agua", "electrico", "psiquico",
        "hierba", "hierba", "electrico", "fuego", "fuego"
    ]
    nombres = [
        "ratata", "charmander", "squirtle", "pikachu", "mew",
        "bulbasaur", "venusaur", "pichu", "charizard", "magmar"
    ]
    ataque = [
        10, 15, 15, 15, 60, 15, 25, 10, 35, 25
    ]

    tipo_pokemon_buscar = 'fuego'
    indices = buscar_indices_tipo_poke(condicion, tipo_pokemon_buscar)
    print(indices)
    # 3 y 7

    print(f'Información de Pokémons tipo: {tipo_pokemon_buscar}')
    # NOMBRE | TIPO | PODER_ATQ
    for indice_poke in indices:
        datos_pokemon = f"{nombres[indice_poke]} | {condicion[indice_poke]} | {ataque[indice_poke]}"
        print(datos_pokemon)