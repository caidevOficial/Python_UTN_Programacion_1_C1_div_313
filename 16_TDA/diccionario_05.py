pokemon = {
    "id": 244,
    "nombre": "entei",
    "tipo": "fuego",
    "poder": 30,
    "condicion": "legendario"
}


# claves = list(pokemon.keys())

# clave_elegida = input(f'Seleccione una clave entre las siguientes {claves}: ')

# valor_actual = pokemon.get(clave_elegida)
# print(f'Valor actual de la clave elegida: {clave_elegida} : {valor_actual}')

# nuevo_valor = input(f'Escriba un nuevo valor: ')

print(pokemon.pop('region', 'Clave no encontrada'))

# print(f'Valor actual de la clave elegida: {clave_elegida} : {pokemon.get(clave_elegida)}')
print(pokemon)