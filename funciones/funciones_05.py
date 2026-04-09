def validar_dato_usuario(min: int, max: int) -> int:
    """Valida el input del usuario para acceder a las opciones del menú

    Args:
        min (int): la minima opcion del menu
        max (int): la maxima opcion del menu

    Returns:
        int: la opcion correcta parseada a entero
    """
    opcion = ''

    while opcion == '' or not opcion.isnumeric() or\
          (min > int(opcion) or max < int(opcion)):
        opcion = input(f'Escriba en numero entre [{min}-{max}]: ')

    return int(opcion)

def validar_numero_entero() -> int:
    opcion = ''

    while opcion == '' or not opcion.isnumeric():
        opcion = input(f'Escriba en numero entero: ')

    return int(opcion)

def obtener_opciones_menu() -> str:
    mensaje =\
    """
    1 - Verificar si un numero es primo
    2 - Verificar si un numero es par
    3 - Salir
    """
    return mensaje

def mostrar_menu(texto_menu: str) -> None:
    print(texto_menu)
    return None

def es_par(numero: int) -> bool:
    # num_par = numero % 2 == 0
    # return num_par
    es_par = False
    if numero % 2 == 0:
        es_par = True
    return es_par

def verificar_numero_par():
    condicion_par = ''
    numero = validar_numero_entero()
    num_par = es_par(numero)
    if not num_par:
        condicion_par = 'NO '
    mensaje = f'El numero {numero} {condicion_par}es PAR'
    print(mensaje)
    return None

def buscar_divisor(numero: int, min_rango: int, max_rango: int) -> bool:
    no_hay_divisor = True
    for num in range(min_rango, max_rango):
        if numero % num == 0:
            no_hay_divisor = False
            break
    return no_hay_divisor

def es_primo(numero: int) -> bool:
    if numero < 2:
        cond_primo = False
    elif numero == 2:
        cond_primo = True
    else:
        # Tenemos en cuenta que ya tiene dos divisores
        # el 1 y el mismo numero, con encontrar otro
        # que no sean los mencionados, el numero NO es primo
        cond_primo = buscar_divisor(numero=numero, min_rango=2, max_rango=numero)

    return cond_primo


def verificar_si_es_primo() -> None:
    condicion_primo = ''
    numero = validar_numero_entero()
    num_primo = es_primo(numero)
    if not num_primo:
        condicion_primo = 'NO '
    mensaje = f'El numero {numero} {condicion_primo}es PRIMO'
    print(mensaje)
    return None


def correr_aplicacion():
    """
    Maneja el flujo principal de la aplicación
    """
    corriendo = True

    while corriendo:

        # mostrar el menú
        texto = obtener_opciones_menu()
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
    
    return None

# Invocamos la funcion para que corra el programa
correr_aplicacion()