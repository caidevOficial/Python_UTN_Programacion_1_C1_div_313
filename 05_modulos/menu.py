# print(f'Modulo MENU se llama: {__name__}')
from variables import (
    DECORADOR, APP_NOMBRE, VERSION
)

def obtener_opciones_menu(nombre_usuario: str) -> str:
    mensaje =\
    f"""
    Usuario Actual: {nombre_usuario}

    1 - Verificar si un numero es primo
    2 - Verificar si un numero es par
    3 - Salir
    """
    return mensaje

def mostrar_menu(texto_menu: str) -> None:
    print(texto_menu)
    return None

def obtener_datos_app():
    """
    Crea un texto con formato:
    decorador nombre version decorador

    Returns:
            Un string con los datos de la aplicación
    """
    texto = f'{DECORADOR} {APP_NOMBRE} {VERSION} {DECORADOR}'
    return texto