from utn_fra_datasets.datasets import lista_dict_pokemones, lista_diccionario_heroes_small


# print(lista_dict_pokemones)

#id,nombre,tipo,poder,condicion

lista_informacion = []
for pokemon in lista_dict_pokemones:
    id_poke = pokemon.get('id')
    nombre = pokemon.get('nombre')
    lista_tipo = pokemon.get('tipo') #
    tipo = lista_tipo[0]
    poder = pokemon.get('poder')
    condicion = pokemon.get('condicion')

    info = f'{id_poke},{nombre},{tipo},{poder},{condicion}'
    lista_informacion.append(info)

for info_poke in lista_informacion:
    print(info_poke)