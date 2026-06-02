matriz_pokemons_t = [
    [244,'entei','fuego',30,'legendario'],
    [28,'sandslash','suelo',15,'normal'],
    [584,'vanilluxe','hielo',15,'normal'],
    [26,'raichu','eléctrico',20,'normal'],
    [9,'blastoise','agua',18,'normal']
]

lista_poke: list[dict] = []

for fila in matriz_pokemons_t:

    poke_actual = {
        "id": fila[0],
        "nombre": fila[1],
        "tipo": fila[2],
        "poder": fila[3],
        "condicion": fila[4]
    }
    lista_poke.append(poke_actual)

# for pokemon in lista_poke:
#     print(pokemon)
#     print(pokemon.get('nombre'))
#     print(f'Cantidad de claves: {len(list(pokemon.keys()))}')

for pokemon in lista_poke:

    # Recorremos las claves del diccionario
    # for key in pokemon.keys():
    #     print(pokemon.get(key))
    
    # Recorremos los valores del diccionario
    # for valor in pokemon.values():
    #     print(valor)
    
    # Recorremos en simultaneo claves y valores
    for clave,valor in pokemon.items():
        print(f"{clave}:{valor}")