encontre_a_pepe = False
encuestados = 0

while not encontre_a_pepe or encuestados < 5:

    nombre = input('Nombre: ')
    if nombre == 'pepe':
        encontre_a_pepe = True
        # break
    else:
        encuestados += 1

mensaje =\
f'''
Personas antes de pepe: {encuestados}
Encontre a pepe? {encontre_a_pepe}
'''
print(mensaje)