from funciones import leer_json, escribir_json
from variables import ARCHIVO_USUARIOS

def pedir_usuario():
    return input('Usuario: ')

def pedir_password():
    return input('Password: ')

def obtener_usuarios(ruta: str) -> list[dict]:
    usuarios = leer_json(ruta)
    lista_usuarios = usuarios.get('usuarios')
    return lista_usuarios

def verificar_password(password_buscada: str, datos_usuario: dict):
    return password_buscada == datos_usuario.get('password')

def filtrar_usuarios_por_username(usuarios: list[dict], username) -> dict:
    usuario_encontrado = {}

    for usuario in usuarios:
        if usuario.get('username') == username and not usuario.get('esta_online'):
            usuario_encontrado = usuario
            break

    return usuario_encontrado

def iniciar_sesion(lista_usuarios_sistema: list[dict]) -> dict:
    username = pedir_usuario()
    password = pedir_password()

    usuario_encontrado = filtrar_usuarios_por_username(lista_usuarios_sistema, username)

    if usuario_encontrado and verificar_password(password, usuario_encontrado):
        usuario_encontrado['esta_online'] = True
        escribir_json(ARCHIVO_USUARIOS, {"usuarios": lista_usuarios_sistema})
        return usuario_encontrado
    return iniciar_sesion(lista_usuarios_sistema)

def cerrar_sesion(lista_usuarios_sistema: list[dict], usuario_actual: dict):
    if usuario_actual:
        usuario_actual['esta_online'] = False
        escribir_json(ARCHIVO_USUARIOS, {'usuarios': lista_usuarios_sistema})
        print('LOG OFF')
        usuario_actual = {}
        lista_usuarios_sistema = list()
    return False

def obtener_menu(usuario: dict):
    mensaje = '1 - Login\n'
    if usuario:
        mensaje += '2 - Saludar Usuario\n'
    return mensaje

def obtener_menu_admin(usuario: dict):
    mensaje = ''
    if usuario and usuario.get('tipo') == 'ADMIN':
        mensaje += '3 - Saludar a Messi\n'
    return mensaje

def obtener_menu_salir():
    mensaje = '4 - Salir\n'
    return mensaje

def imprimir_menu(menu: str):
    print(menu)

def saludar_usuario(usuario: dict):
    if usuario:
        print(f'Bienvenido al sistema, USUARIO: {usuario.get("username")}')
    else:
        print('Primero tiene que loguear en el sistema')

def cargar_usuarios_si_corresponde(lista_usuarios: list[dict]) -> list[dict]:
    if not lista_usuarios:
        lista_usuarios = obtener_usuarios(ARCHIVO_USUARIOS)
        print('USUARIOS CARGADOS')
    return lista_usuarios

def correr_aplicacion():
    usuario = {}
    lista_usuarios_sistema = []

    corriendo = True
    while corriendo:
        menu = obtener_menu(usuario)
        menu += obtener_menu_admin(usuario)
        menu += obtener_menu_salir()
        imprimir_menu(menu)
        opcion = int(input('Ingrese una opcion: '))
        
        match opcion:
            case 1:
                if not usuario:
                    lista_usuarios_sistema = cargar_usuarios_si_corresponde(lista_usuarios_sistema)
                    usuario = iniciar_sesion(lista_usuarios_sistema)
                else:
                    print(f'YA ESTA LOGEADO CON: {usuario.get("username")}')
            case 2:
                saludar_usuario(usuario)
            case 3:
                pass
            case 4:
                #################################
                print('SALIENDO DEL PROGRAMA')
                print(lista_usuarios_sistema)
                corriendo = cerrar_sesion(lista_usuarios_sistema, usuario)

if __name__ == '__main__':
    correr_aplicacion()