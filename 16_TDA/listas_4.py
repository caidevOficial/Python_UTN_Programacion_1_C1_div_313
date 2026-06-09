import copy

lista_original = [
    ["Pepe", "Moni"],
    ["Goku", "Vegeta"],
    ["Itadori", "Gojo"]
]

# Shallow Copy - Superficial
lista_copia = copy.copy(lista_original)
lista_copia = lista_original.copy()
lista_copia = lista_copia[:]

# lista_copia[1] = ["Trunks", "Gohan"]


# for fila in lista_copia:
#     fila[0] = {"nombre": fila[0]}
#     fila[1] = {"nombre": fila[1]}

for indice_fila in range(len(lista_copia)):
    # lista_copia[indice_fila][0] = {"nombre": lista_copia[indice_fila][0]}
    # lista_copia[indice_fila][1] = {"nombre": lista_copia[indice_fila][1]}

    # lista_copia[indice_fila] = [
    #     {"nombre": lista_copia[indice_fila][0]},
    #     {"nombre": lista_copia[indice_fila][1]}
    # ]

    lista_copia[indice_fila] = list(
        [
            lista_copia[indice_fila][0],
            lista_copia[indice_fila][1]
        ]
    )

    lista_copia[indice_fila] = list(lista_copia[indice_fila])

lista_original[1][0] = "Trunks"

print(lista_original)
print(lista_copia)

print('Referencia de memoria de las matrices')
print(f'DIR MEM ORIGINAL: {hex(id(lista_original))}')
print(f'DIR MEM COPIA: {hex(id(lista_copia))}')


for fila_o, fila_c in zip(lista_original, lista_copia):
    print('\nReferencia de memoria de las filas de las matrices')
    print(f'DIR MEM ORIGINAL: {hex(id(fila_o))} - VALOR:{fila_o}')
    print(f'DIR MEM COPIA: {hex(id(fila_c))} - VALOR:{fila_c}')

    
    for elem_o, elem_c in zip(fila_o, fila_c):
        print('\nReferencia de memoria de los elementos de cada fila de las matrices')
        print(f'DIR MEM ORIGINAL: {hex(id(elem_o))} - VALOR:{elem_o}')
        print(f'DIR MEM COPIA: {hex(id(elem_c))} - VALOR:{elem_c}')
        # print(f'DIR MEM COPIA DICC: {hex(id(elem_c.get('nombre')))} - VALOR:{elem_c.get('nombre')}')