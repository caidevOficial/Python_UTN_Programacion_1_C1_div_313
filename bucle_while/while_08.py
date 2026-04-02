# queremos validar de que el usuario sea mayor de edad (18-89)

edad_usuario = ''

while edad_usuario == '' or\
    not edad_usuario.isnumeric() or\
    not (18 <= int(edad_usuario) <= 89):
    edad_usuario = input('Ingrese su edad: ')
    
    # if int(edad_usuario) > 89 or int(edad_usuario) < 18:
    #     pass

edad_usuario_int = int(edad_usuario)
print(f'Edad correcta: {edad_usuario_int}')