mi_texto = "Este es un texto de \"EJEMPLO\", 'DE TEXTO', 'PYTHON' "
mi_texto = """ Este es 'un' "EJEMPLO" """


print(mi_texto)


print(mi_texto[7])

for caracter in mi_texto:
    print(caracter)

for indice_caracter in range(len(mi_texto)):
    print(mi_texto[indice_caracter])
