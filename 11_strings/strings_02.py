mi_lista = ["pepe", "moni"]
mi_texto = ""



# print(hex(id(mi_lista)))
print(hex(id(mi_texto)))

mi_lista.append('Fatiga')

for nombre in mi_lista:
    mi_texto = f'{mi_texto}, {nombre}'
    print(hex(id(mi_texto)))

# print(hex(id(mi_lista)))