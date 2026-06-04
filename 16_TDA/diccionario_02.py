pokemon = {
    "id": 244,
    "nombre": "entei",
    "tipo": "fuego",
    "poder": 30,
    "condicion": "legendario"
}


# nombre = pokemon["region"]
nombre = pokemon.get("REGION", 'n/a')
print(f'VALOR: {nombre}')


