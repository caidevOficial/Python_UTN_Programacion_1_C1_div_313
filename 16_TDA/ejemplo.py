import os

def menu_productos():
    corriendo = True

    while corriendo:
        print('MENU productos')
        print('1 - MOSTRAR MENSAJE\n2 - SALIR')
        opcion = input('ingrese opcion: ')
        match opcion:
            case '1':
                print('ESTOY EN LA OPCION 1 DE LA SECCION PRODUCTOS')
            case '2':
                corriendo = False
        os.system('pause')
        os.system('cls')
                

def aplicacion():
    corriendo = True

    while corriendo:
        print('MENU PRINCIPAL')
        print('1 - IR A OPCION 1\n2 - IR A OPCION 2\n3 - SALIR')
        opcion = input('ingrese opcion: ')
        match opcion:
            case '1':
                print('ESTOY EN LA OPCION 1 DEL MENU PRINCIPAL')
                menu_productos()
            case '2':
                print('ESTOY EN LA OPCION 2 DEL MENU PRINCIPAL')
            case '3':
                corriendo = False
        os.system('pause')
        os.system('cls')


aplicacion()