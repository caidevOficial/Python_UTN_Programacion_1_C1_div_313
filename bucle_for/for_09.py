
corriendo = True

while corriendo:

    mensaje=\
    """
    1 - Mostrar tabla de multiplicación de X número
    2 - Mostrar numeros de forma DES hasta el 0 inclusive
    3 - Salir
    """
    print(mensaje)

    opcion_str = ''

    while opcion_str != '1' and\
          opcion_str != '2' and\
          opcion_str != '3':
        opcion_str = input('Ingrese su opcion: ')
    
    match opcion_str:
        case '1':
            numero_user = ''

            while numero_user == '' or\
                not numero_user.isnumeric():
                numero_user = input('Ingrese un número para ver su tabla de multiplicación: ')
            numero_int = int(numero_user)

            print('________________________________')
            for num_a in range(1, 11):
                resultado = num_a * numero_int
                print(f'{numero_int} X {num_a} = {resultado}')
            print('________________________________')
        case '2':
            numero_user = ''
            while numero_user == '' or\
                not numero_user.isnumeric():
                numero_user = input('Ingrese un número: ')
            numero_int = int(numero_user)

            print('________________________________')
            
            for num in range(numero_int, -1, -1):
                print(num)
            print('________________________________')

        case '3':
            print('Saliendo del programa')
            corriendo = False