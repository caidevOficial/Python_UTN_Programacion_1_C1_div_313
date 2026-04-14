from menu import (
    mostrar_menu, 
    obtener_opciones_menu,
    obtener_datos_app
)

from verificaciones import (
    verificar_numero_par, verificar_si_es_primo
)

from validaciones import (
    validar_dato_usuario, validar_nombre
)
import variables as var
import os

def correr_aplicacion():
    """
    Maneja el flujo principal de la aplicación
    """
    datos_app = obtener_datos_app()

    print(datos_app)

    corriendo = True
    nombre_usuario = validar_nombre()

    while corriendo:
        
        # mostrar el menú
        texto = obtener_opciones_menu(nombre_usuario)
        mostrar_menu(texto)
        opcion_elegida = validar_dato_usuario(min=1, max=3)

        match opcion_elegida:
            case 1:
                verificar_si_es_primo()
            case 2:
                verificar_numero_par()
            case 3:
                print('Saliendo del programa')
                corriendo = False
        
        print(f'{var.DECORADOR} {var.DECORADOR}')

        os.system('pause')
        os.system('cls')

    return None