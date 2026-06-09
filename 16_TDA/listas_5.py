import copy

lista_original = [
    ["Pepe", "Moni"],
    ["Goku", "Vegeta"],
    ["Itadori", "Gojo"]
]

# Deep Copy - Profunda
lista_copia = copy.deepcopy(lista_original)

# lista_copia[1] = ["Trunks", "Gohan"]
lista_copia[1][0] = "Trunks"


for fila in lista_copia:
    fila[0] = {"nombre": fila[0]}
    fila[1] = {"nombre": fila[1]}


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
        print(f'DIR MEM COPIA DICC: {hex(id(elem_c.get('nombre')))} - VALOR:{elem_c.get('nombre')}')




"""
goku
vegeta
pepe
moni
gohan

L_O_1 = [F38, F39]
L_O_2 = [F40, F41]

L_C_1 = [F39, F42]
L_C_2 = [F41, F40]

M_O = [F43, F44]

M_C = [F46, F47]
"""