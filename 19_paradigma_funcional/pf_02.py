from utn_fra_datasets.datasets import lista_dict_pokemones

def es_tipo_fuego(pokemon: dict) -> bool:
    return pokemon.get('tipo')[0] == 'fuego'

def es_legendario(pokemon: dict) -> bool:
    return pokemon.get('condicion') == 'legendario'

def es_condicion(pokemon: dict, condicion: str) -> bool:
    return pokemon.get('condicion') == condicion

def es_condicion_v2(pokemon: dict, clave: str, valor: str) -> bool:
    return pokemon.get(clave) == valor

def es_normal(pokemon: dict) -> bool:
    return pokemon.get('condicion') == 'normal'

def filtrar_pokemones(pokemones: list[dict], condicion_filtro: str, callback_filtro):
    filtrados = []

    for pokemon in pokemones:
        if callback_filtro(pokemon, condicion_filtro):
            filtrados.append(pokemon)
    
    print('Pokemones filtrados')
    for pokemon in filtrados:
        print(pokemon)



def filtrar_pokemones_v2(pokemones: list[dict], configs: dict):
    filtrados = []

    for pokemon in pokemones:
        if configs.get('funcion_1')(pokemon, configs.get('clave_1'), configs.get('valor_1')) and\
            configs.get('funcion_1')(pokemon, configs.get('clave_2'), configs.get('valor_2')):
            filtrados.append(pokemon)
    
    print('Pokemones filtrados')
    for pokemon in filtrados:
        print(pokemon)

# filtrar_pokemones(lista_dict_pokemones, 'legendario', es_condicion)
print()
# filtrar_pokemones(lista_dict_pokemones, es_tipo_fuego)
configs = {
    "funcion_1": es_condicion_v2,
    "clave_1": 'tipo',
    "valor_1": ['fuego'],
    "clave_2": 'condicion',
    "valor_2": 'legendario'
}
filtrar_pokemones_v2(lista_dict_pokemones, configs)