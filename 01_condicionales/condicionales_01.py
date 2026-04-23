edad_usuario_str = input("Escriba su edad: ")
genero_usuario_str = input('Ingrese su género (M - F): ')

edad_usuario_int = int(edad_usuario_str)


"""
F -> 60
M -> 65
"""
# if edad_usuario_int >= 65:
#     if genero_usuario_str == 'M':
#         print('Es usted una persona jubilada')

# elif edad_usuario_int >= 60:
#     if genero_usuario_str == 'F':
#         print('Es usted una persona jubilada')
#     else:
#         print('NO Es usted una persona jubilada')

if (edad_usuario_int >= 65):
    
    lo_esta = input('Actualmente esta jubilado? [S-N]: ')
    if lo_esta == 'S':
        print('Actualmente esta jubilado, no se puede dar de alta nuevamente.')
    else:
        print('Actualmente no esta jubilado, se puede jubilar ahora mismo')

elif (edad_usuario_int >= 60) and (genero_usuario_str == 'F'):
    print('se puede jubilar')
else:
    print('no se puede jubilar')
