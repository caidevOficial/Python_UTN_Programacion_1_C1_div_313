
def parsear_matriz_lista(matriz: list[list], lista_claves: list[str]) -> list[dict]:

    lista_dataset = []

    for fila in matriz:
        datos_prod = {}

        for indice_clave in range(len(lista_claves)):
            
            clave = lista_claves[indice_clave]
            valor = fila[indice_clave]

            datos_prod[clave] = valor
        lista_dataset.append(datos_prod)
    
    return lista_dataset


# from datasets import productos

# print(
#     parsear_matriz_lista(productos, ['id', 'nombre', 'stock', 'precio_unitario'])
# )